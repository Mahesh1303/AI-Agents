import datetime
from zoneinfo import ZoneInfo
from google.adk.agents import Agent



def job_analyzer(city: str, job_title: str = "Fullstack Developer", time_filter: int = 86400) -> dict:
    """Structures the job search URL for LinkedIn based on city, job title, and custom time filter.
       Allows any custom time value for the f_TPR parameter.

    Args:
        city (str): The city to search for jobs in.
        job_title (str, optional): The job title to search for. Defaults to "Fullstack Developer".
        time_filter (int, optional): The custom time filter for job postings in seconds. Defaults to 86400 (Past 24 hours).

    Returns:
        dict: A dictionary with status and result (URL), or error message.
    """
    
    if not city:
        return {
            "status": "error",
            "message": "City parameter is required."
        }
    
    job_title_encoded = job_title.replace(" ", "%20")
    city_encoded = city.replace(" ", "%20")
    
    time_filter_str = f"r{time_filter}"

    linkedin_url = f"https://www.linkedin.com/jobs/search-results/?f_TPR={time_filter_str}&keywords={job_title_encoded}&location={city_encoded}"

    return {
        "status": "success",
        "result": {
            "job_title": job_title,
            "city": city,
            "time_filter": time_filter_str,
            "linkedin_url": linkedin_url
        }
    }






root_agent = Agent(
    name="Job_Search_Agent",
    model="gemini-2.0-flash",
    description=(
        "Helpful agent for job search."
    ),
    instruction=(
        "You are a helpful agent who can assist user  about the jobs and job search on LinkedIn."
    ),
    tools=[ job_analyzer],
)