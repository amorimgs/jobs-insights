from typing import Union, List, Dict
from src.insights.jobs import ProcessJobs


class ProcessSalaries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_max_salary(self) -> int:
        salaries = list(
            job["max_salary"] for job in self.jobs_list if job["max_salary"]
        )
        return max(int(s) for s in salaries if s.isdigit())

    def get_min_salary(self) -> int:
        salaries = list(
            job["min_salary"] for job in self.jobs_list if job["min_salary"]
        )
        return min(int(s) for s in salaries if s.isdigit())

    def matches_salary_range(self, job: Dict, salary: Union[int, str]) -> bool:
        try:
            min_salary = job.get("min_salary")
            max_salary = job.get("max_salary")

            min_salary = (
                int(min_salary)
                if isinstance(min_salary, str) and min_salary.isdigit()
                else min_salary
            )
            max_salary = (
                int(max_salary)
                if isinstance(max_salary, str) and max_salary.isdigit()
                else max_salary
            )
            salary = (
                int(salary)
                if isinstance(salary, str) and salary.isdigit()
                else salary
            )

            if (
                not all(
                    isinstance(i, int)
                    for i in [min_salary, max_salary, salary]
                )
                or max_salary < min_salary
            ):
                raise ValueError()

            return min_salary <= salary <= max_salary
        except ValueError:
            raise ValueError()

    def filter_by_salary_range(
        self, jobs: List[dict], salary: Union[str, int]
    ) -> List[Dict]:
        pass
