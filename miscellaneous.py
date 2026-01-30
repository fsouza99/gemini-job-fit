from datetime import datetime
from string import Template
import re

from constants import PROMPTS
from myio import read_file


def company_name(job_url: str) -> str:
    """Get company name from a Gupy's job page URL.

    URL has format:
        https://<company>.gupy.io/jobs/<id>?jobBoardSource=share_link
    """
    return job_url[8:job_url.index('.gupy.')].capitalize()


def curr_date() -> str:
    """Get current date as string."""
    return str(datetime.today().date())


def clean_title(title: str) -> str:
    """Remove characters that could hinder file creation."""
    return re.sub(r'[\\/:*<>|"]', '_', title)


def create_prompt(
    prompt_key: str,
    job_position: str,
    job_description: str,
    cv_path: str) -> str:
    """Build prompt from selected prompt template, CV file and job info."""
    template = PROMPTS.get(prompt_key)
    if template is None:
        raise Exception(
            f'No prompt file is referred by given key "{prompt_key}".')
    return Template(
        read_file(template)).substitute(
            job_position=job_position.lower(),
            job_description=job_description,
            curriculum=read_file(cv_path))


def create_path_prefix(output_dir: str, *args) -> str:
    """Build prefix for the path of output file."""
    buffer = ' - '.join([clean_title(element) for element in args])
    return f"{output_dir}\\{buffer}"

