from datetime import datetime
from string import Template
import re

from constants import PROMPT_FILE
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
    job_position: str, job_description: str, template_path: str) -> str:
    """Build prompt from template."""
    return Template(
        read_file(PROMPT_FILE)).substitute(
            job_position=job_position.lower(),
            job_description=job_description,
            curriculum=read_file(template_path))


def create_path_prefix(
    output_dir: str, company_name: str, job_position: str) -> str:
    """Generate prefix for the path of output file."""
    cleaned_cn = clean_title(company_name)
    cleaned_jp = clean_title(job_position)
    return f"{output_dir}\\{cleaned_cn} - {cleaned_jp}"

