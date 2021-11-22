sudo docker build -t docker_ctm_python .
docker run --rm -p 8787:8787 -v $(PWD):/opt/notebooks docker_ctm_python /bin/bash -c \
"jupyter notebook --ip=0.0.0.0 --port=8787 --notebook-dir=/opt/notebooks --allow-root --no-browser"
