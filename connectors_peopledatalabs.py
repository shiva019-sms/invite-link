import httpx

API_KEY = "YOUR_PDL_API_KEY"  # Replace with your actual API key

async def get_person_data(full_name, company=None):
    url = "https://api.peopledatalabs.com/v5/person/enrich"
    params = {
        "api_key": API_KEY,
        "name": full_name
    }
    if company:
        params["company"] = company
    async with httpx.AsyncClient() as client:
        resp = await client.get(url, params=params)
        if resp.status_code == 200:
            return resp.json().get("data", {})
        return {}