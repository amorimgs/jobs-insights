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
        result = bool()
        try:
            if "min_salary" not in job or "max_salary" not in job:
                raise ValueError()
            min_salary = job["min_salary"]
            max_salary = job["max_salary"]
            if type(min_salary) != str and type(min_salary) != int:
                raise ValueError()
            if type(max_salary) != str and type(max_salary) != int:
                raise ValueError()
            if type(salary) != str and type(salary) != int:
                raise ValueError()
            if type(min_salary) == str:
                if not min_salary.isdigit():
                    raise ValueError()
                min_salary = int(min_salary)
            if type(max_salary) == str:
                if not max_salary.isdigit():
                    raise ValueError()
                max_salary = int(max_salary)
            if max_salary < min_salary:
                raise ValueError()
            if type(salary) == str:
                if not salary.isdigit():
                    raise ValueError()
                salary = int(salary)
            result = min_salary <= salary <= max_salary
        except ValueError:
            raise ValueError()
        return result

    def filter_by_salary_range(
        self, jobs: List[dict], salary: Union[str, int]
    ) -> List[Dict]:
        pass
