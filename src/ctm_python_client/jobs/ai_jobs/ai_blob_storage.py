from ctm_python_client.jobs.ai_jobs.ai_generic import AiGenericJob


class AIBlobStorageJob(AiGenericJob):
    def __init__(
        self,
        folder,
        job_name,
        connection_profile,
        ai_action,
        ai_blob_name,
        ai_container,
        ai_file_path,
        ai_public_access,
        host=None,
        run_as=None,
        description=None,
    ):
        params_dict = {
            "AI-Action": ai_action,
            "AI-Blob name (Up/Download)": ai_blob_name,
            "AI-Container (Up/Download)": ai_container,
            "AI-File path": ai_file_path,
            "AI-Public Access": ai_public_access,
        }

        AiGenericJob.__init__(
            self,
            folder=folder,
            job_name=job_name,
            connection_profile=connection_profile,
            ai_name="AI Blob Storage",
            host=host,
            run_as=run_as,
            description=description,
            **params_dict
        )
