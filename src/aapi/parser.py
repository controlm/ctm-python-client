import aapi
import attrs
import enum
import typing
import inspect


class _AAPIParser:

    def _get_properties(self, cls):
        res = {'class': cls, 'fields': {},
               'classes': {}, 'enums': {}, 'containers': {}}
        for field in attrs.fields(cls):
            repr = field.metadata.get('_aapi_repr_')
            if repr:
                if not field.init:
                    continue
                res['fields'][repr] = field
            else:
                if '_abstract_aapi_container_' in field.metadata:
                    if field.name == 'dates_list':
                        continue
                    tp_l = field.type.split('[')[1].split(']')[0]
                    if tp_l == 'Flow':
                        continue
                    tp_l = [m[1] for m in inspect.getmembers(
                        aapi, inspect.isclass) if m[0] == tp_l][0]
                    res['containers'][tp_l] = field

        for member in inspect.getmembers(cls, inspect.isclass):
            if member[0] == '__class__':
                continue
            if attrs.has(member[1]):
                res['classes'][member[0]] = self._get_properties(member[1])
            elif issubclass(member[1], enum.Enum):
                res['enums'][member[0]] = member[1]

        return res

    def _init_parser(self):
        self.DCT_CLASS = {}
        for member in inspect.getmembers(aapi, inspect.isclass):
            if not attrs.has(member[1]):
                continue
            tp = attrs.fields_dict(member[1]).get('_type')
            if not tp:
                self.DCT_CLASS[member[0]
                               ] = self._get_properties(member[1])
            else:
                self.DCT_CLASS[tp.default] = self._get_properties(
                    member[1])

                # add a copy with the class name
                self.DCT_CLASS[member[0]
                               ] = self._get_properties(member[1])
        # return self.DCT_CLASS

    def __init__(self) -> None:
        self._init_parser()

    def parse_list_object(self, lst: typing.List[typing.Dict[str, typing.Any]], cls_dct):
        res = []
        for obj in lst:
            o = self.parse_object(obj=obj, cls_dct=cls_dct)
            res.append(o)

        return res

    def parse_object(self, obj: typing.Dict[str, typing.Any], cls_dct, additional_kwargs: typing.Dict[str, typing.Any] = None) -> typing.Any:
        kwargs = {}

        # check for containers
        for container_class in cls_dct['containers'].values():
            kwargs[container_class.name] = []

        for k, v in obj.items():
            if k in cls_dct['fields']:
                if isinstance(v, dict):
                    if k in cls_dct['classes']:
                        val = self.parse_object(v, cls_dct['classes'][k])
                elif isinstance(v, list):
                    tp_ = cls_dct['fields'][k].type.split('[')[1].split(']')[0]
                    if tp_ == 'typing.Dict' or tp_ == 'str':
                        val = v

                    else:
                        val = self.parse_list_object(v, self.DCT_CLASS[tp_])
                else:
                    if cls_dct['fields'][k].type in cls_dct['enums']:
                        val = cls_dct['enums'][k](v)
                    else:
                        val = v

                kwargs[cls_dct['fields'][k].name] = val
            else:
                if k == 'Type':
                    continue
                if isinstance(v, dict):
                    if 'Type' in v:
                        o = self.parse_typed_object(k, v)

                        # check if object type is from a container
                        for container, cv in cls_dct['containers'].items():
                            if isinstance(o, container):
                                kwargs[cv.name].append(o)
                    else:
                        pass
                else:
                    pass

        if additional_kwargs:
            kwargs.update(additional_kwargs)
        return cls_dct['class'](**kwargs)

    def parse_typed_object(self, objname: str, obj: typing.Dict[str, typing.Any]) -> typing.Any:
        tp = obj.get('Type')
        cls_dct = self.DCT_CLASS[tp]

        return self.parse_object(obj, cls_dct, {'object_name': objname})


AAPIParser = _AAPIParser()