from typing import List, Dict
import csv


class ProcessJobs:
    def __init__(self) -> None:
        self.jobs_list = list()

    def read(self, path) -> List[Dict]:
        with open(path, "r") as file:
            files = csv.DictReader(file)
            self.jobs_list = [row for row in files]

    def get_unique_job_types(self) -> List[str]:
        return list(set([job["job_type"] for job in self.jobs_list]))

    def filter_by_multiple_criteria(self, jobs, d) -> List[dict]:
        param_industry = d["industry"]
        param_job_type = d["job_type"]
        result = list(
            n
            for n in jobs
            if n["industry"] == param_industry
            and n["job_type"] == param_job_type
        )
        return result
