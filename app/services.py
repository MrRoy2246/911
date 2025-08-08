# from datetime import datetime, timedelta
# from typing import Dict, List, Any, Optional
# import httpx
# import json
# from .config import CITY_REGISTRY, APP_CONFIG

# def build_soql_filter(date_field: str, hours: int) -> str:
#     """Build SoQL filter for retrieving data from the last X hours"""
#     start_time = datetime.utcnow() - timedelta(hours=hours)
#     # Format for SoQL: date_field >= 'YYYY-MM-DDTHH:MM:SS'
#     return f"{date_field} >= '{start_time.isoformat()}'"

# def set_nested_value(data_dict: Dict, keys: List[str], value: Any) -> None:
#     """Set a value in a nested dictionary using dot notation keys"""
#     if len(keys) == 1:
#         data_dict[keys[0]] = value
#     else:
#         key = keys[0]
#         if key not in data_dict:
#             data_dict[key] = {}
#         set_nested_value(data_dict[key], keys[1:], value)

# def normalize_record(record: Dict, field_mapping: Dict, city: str) -> Dict:
#     """Normalize a city-specific record to standard format"""
#     normalized = {"city": city}
    
#     for source_field, normalized_field in field_mapping.items():
#         if source_field in record:
#             # Handle nested fields using dot notation
#             if "." in normalized_field:
#                 keys = normalized_field.split(".")
#                 set_nested_value(normalized, keys, record[source_field])
#             else:
#                 normalized[normalized_field] = record[source_field]
    
#     # Ensure required fields exist
#     if "timestamp" not in normalized:
#         normalized["timestamp"] = None
#     if "incident_type" not in normalized:
#         normalized["incident_type"] = "Unknown"
    
#     # Add city-specific fields if they exist
#     if city == "san_francisco":
#         # San Francisco specific processing
#         if "call_id" not in normalized and "cad_number" in record:
#             normalized["call_id"] = record["cad_number"]
#         if "priority" not in normalized and "priority_final" in record:
#             normalized["priority"] = record["priority_final"]
#         if "agency" not in normalized and "agency" in record:
#             normalized["agency"] = record["agency"]
#         if "disposition" not in normalized and "disposition" in record:
#             normalized["disposition"] = record["disposition"]
#         if "onview_flag" not in normalized and "onview_flag" in record:
#             normalized["onview_flag"] = record["onview_flag"]
#         if "sensitive_call" not in normalized and "sensitive_call" in record:
#             normalized["sensitive_call"] = record["sensitive_call"]
    
#     return normalized

# async def fetch_city_data(city: str, hours: int) -> List[Dict]:
#     """Fetch emergency call data from a city's API"""
#     if city not in CITY_REGISTRY:
#         raise ValueError(f"City '{city}' is not supported")
    
#     city_config = CITY_REGISTRY[city]
    
#     # Build the API URL
#     base_url = city_config["base_url"]
#     dataset_id = city_config["dataset_id"]
#     url = f"{base_url}{dataset_id}.json"
    
#     # Start with default parameters
#     params = city_config.get("api_params", {}).copy()
    
#     # Add SoQL filter if supported
#     if city_config["supports_soql"]:
#         soql_filter = build_soql_filter(city_config["date_field"], hours)
#         params["$where"] = soql_filter
    
#     try:
#         # Fetch data from city API
#         async with httpx.AsyncClient(timeout=APP_CONFIG["timeout"]) as client:
#             response = await client.get(url, params=params)
#             response.raise_for_status()
#             data = response.json()
        
#         # Normalize all records
#         normalized_data = []
#         for record in data:
#             normalized_record = normalize_record(
#                 record, 
#                 city_config["field_mapping"], 
#                 city
#             )
#             normalized_data.append(normalized_record)
        
#         return normalized_data
    
#     except httpx.HTTPStatusError as e:
#         raise httpx.HTTPStatusError(
#             f"Error fetching data from {city} API: {str(e)}",
#             request=e.request,
#             response=e.response
#         )
#     except httpx.RequestError as e:
#         raise httpx.RequestError(f"Service unavailable: Could not connect to {city} API", request=e.request)
#     except json.JSONDecodeError:
#         raise ValueError(f"Error parsing response from {city} API")
#     except Exception as e:
#         raise RuntimeError(f"Unexpected error: {str(e)}")



# --------------------------------------------------




# from datetime import datetime, timedelta
# from typing import Dict, List, Any, Optional
# import httpx
# import json
# from .config import CITY_REGISTRY, APP_CONFIG

# def build_soql_filter(city: str, date_field: str, hours: int) -> str:
#     """Build SoQL filter for retrieving data from the last X hours"""
#     start_time = datetime.utcnow() - timedelta(hours=hours)
    
#     # Get city-specific date format if available
#     city_config = CITY_REGISTRY.get(city, {})
#     date_format = city_config.get("date_format")
    
#     # Format the date according to city-specific requirements
#     if date_format:
#         date_str = start_time.strftime(date_format)
#     else:
#         # Default format with fractional seconds
#         date_str = start_time.isoformat()
    
#     return f"{date_field} >= '{date_str}'"

# def set_nested_value(data_dict: Dict, keys: List[str], value: Any) -> None:
#     """Set a value in a nested dictionary using dot notation keys"""
#     if len(keys) == 1:
#         data_dict[keys[0]] = value
#     else:
#         key = keys[0]
#         if key not in data_dict:
#             data_dict[key] = {}
#         set_nested_value(data_dict[key], keys[1:], value)

# def normalize_record(record: Dict, field_mapping: Dict, city: str) -> Dict:
#     """Normalize a city-specific record to standard format"""
#     normalized = {"city": city}
    
#     # Apply field mapping
#     for source_field, normalized_field in field_mapping.items():
#         if source_field in record:
#             # Handle nested fields using dot notation
#             if "." in normalized_field:
#                 keys = normalized_field.split(".")
#                 set_nested_value(normalized, keys, record[source_field])
#             else:
#                 normalized[normalized_field] = record[source_field]
    
#     # Ensure required fields exist
#     required_fields = ["timestamp", "incident_type"]
#     for field in required_fields:
#         if field not in normalized:
#             normalized[field] = None if field == "timestamp" else "Unknown"
    
#     # Apply city-specific post-processing if defined in config
#     city_config = CITY_REGISTRY.get(city, {})
#     post_processing = city_config.get("post_processing", {})
    
#     for source_field, target_field in post_processing.items():
#         if source_field in record and target_field not in normalized:
#             normalized[target_field] = record[source_field]
    
#     return normalized

# async def fetch_city_data(city: str, hours: int) -> List[Dict]:
#     """Fetch emergency call data from a city's API"""
#     if city not in CITY_REGISTRY:
#         raise ValueError(f"City '{city}' is not supported")
    
#     city_config = CITY_REGISTRY[city]
    
#     # Build the API URL
#     base_url = city_config["base_url"]
#     dataset_id = city_config["dataset_id"]
#     url = f"{base_url}{dataset_id}.json"
    
#     # Start with default parameters
#     params = city_config.get("api_params", {}).copy()
    
#     # Add SoQL filter if supported
#     if city_config.get("supports_soql", False):
#         try:
#             soql_filter = build_soql_filter(city, city_config["date_field"], hours)
#             params["$where"] = soql_filter
#         except Exception as e:
#             # Log the error but continue without the filter
#             print(f"Warning: Could not build SoQL filter for {city}: {str(e)}")
    
#     try:
#         # Fetch data from city API
#         async with httpx.AsyncClient(timeout=APP_CONFIG["timeout"]) as client:
#             response = await client.get(url, params=params)
#             response.raise_for_status()
#             data = response.json()
        
#         # Normalize all records
#         normalized_data = []
#         for record in data:
#             normalized_record = normalize_record(
#                 record, 
#                 city_config["field_mapping"], 
#                 city
#             )
#             normalized_data.append(normalized_record)
        
#         return normalized_data
    
#     except httpx.HTTPStatusError as e:
#         # Try to get more details from the response if available
#         error_details = ""
#         try:
#             error_details = e.response.text
#         except:
#             pass
        
#         raise httpx.HTTPStatusError(
#             f"Error fetching data from {city} API: {str(e)}. Details: {error_details}",
#             request=e.request,
#             response=e.response
#         )
#     except httpx.RequestError as e:
#         raise httpx.RequestError(f"Service unavailable: Could not connect to {city} API", request=e.request)
#     except json.JSONDecodeError as e:
#         raise ValueError(f"Error parsing response from {city} API: {str(e)}")
#     except Exception as e:
#         raise RuntimeError(f"Unexpected error: {str(e)}")
    

# ============================================================


    # federal level test



# from datetime import datetime, timedelta
# from typing import Dict, List, Any, Optional
# import httpx
# import json
# from .config import CITY_REGISTRY, FEDERAL_REGISTRY, APP_CONFIG

# def build_soql_filter(city: str, date_field: str, hours: int) -> str:
#     """Build SoQL filter for retrieving data from the last X hours"""
#     start_time = datetime.utcnow() - timedelta(hours=hours)
    
#     # Get city-specific date format if available
#     city_config = CITY_REGISTRY.get(city, {})
#     date_format = city_config.get("date_format")
    
#     # Format the date according to city-specific requirements
#     if date_format:
#         date_str = start_time.strftime(date_format)
#     else:
#         # Default format with fractional seconds
#         date_str = start_time.isoformat()
    
#     return f"{date_field} >= '{date_str}'"

# def set_nested_value(data_dict: Dict, keys: List[str], value: Any) -> None:
#     """Set a value in a nested dictionary using dot notation keys"""
#     if len(keys) == 1:
#         data_dict[keys[0]] = value
#     else:
#         key = keys[0]
#         if key not in data_dict:
#             data_dict[key] = {}
#         set_nested_value(data_dict[key], keys[1:], value)

# def normalize_record(record: Dict, field_mapping: Dict, city: str) -> Dict:
#     """Normalize a city-specific record to standard format"""
#     normalized = {"city": city}
    
#     # Apply field mapping
#     for source_field, normalized_field in field_mapping.items():
#         if source_field in record:
#             # Handle nested fields using dot notation
#             if "." in normalized_field:
#                 keys = normalized_field.split(".")
#                 set_nested_value(normalized, keys, record[source_field])
#             else:
#                 normalized[normalized_field] = record[source_field]
    
#     # Ensure required fields exist
#     required_fields = ["timestamp", "incident_type"]
#     for field in required_fields:
#         if field not in normalized:
#             normalized[field] = None if field == "timestamp" else "Unknown"
    
#     # Apply city-specific post-processing if defined in config
#     city_config = CITY_REGISTRY.get(city, {})
#     post_processing = city_config.get("post_processing", {})
    
#     for source_field, target_field in post_processing.items():
#         if source_field in record and target_field not in normalized:
#             normalized[target_field] = record[source_field]
    
#     return normalized

# async def fetch_city_data(city: str, hours: int) -> List[Dict]:
#     """Fetch emergency call data from a city's API"""
#     if city not in CITY_REGISTRY:
#         raise ValueError(f"City '{city}' is not supported")
    
#     city_config = CITY_REGISTRY[city]
    
#     # Build the API URL
#     base_url = city_config["base_url"]
#     dataset_id = city_config["dataset_id"]
#     url = f"{base_url}{dataset_id}.json"
    
#     # Start with default parameters
#     params = city_config.get("api_params", {}).copy()
    
#     # Add SoQL filter if supported
#     if city_config.get("supports_soql", False):
#         try:
#             soql_filter = build_soql_filter(city, city_config["date_field"], hours)
#             params["$where"] = soql_filter
#         except Exception as e:
#             # Log the error but continue without the filter
#             print(f"Warning: Could not build SoQL filter for {city}: {str(e)}")
    
#     try:
#         # Fetch data from city API
#         async with httpx.AsyncClient(timeout=APP_CONFIG["timeout"]) as client:
#             response = await client.get(url, params=params)
            
#             # If we get a 400 error, try without the SoQL filter
#             if response.status_code == 400:
#                 print(f"Warning: Got 400 error for {city}, trying without SoQL filter")
#                 # Remove the $where parameter
#                 if "$where" in params:
#                     del params["$where"]
#                 response = await client.get(url, params=params)
                
#                 # If we still get a 400 error, try without the $select parameter
#                 if response.status_code == 400:
#                     print(f"Warning: Still getting 400 error for {city}, trying without $select parameter")
#                     # Remove the $select parameter
#                     if "$select" in params:
#                         del params["$select"]
#                     response = await client.get(url, params=params)
                    
#                     # If we still get a 400 error, try with minimal parameters
#                     if response.status_code == 400:
#                         print(f"Warning: Still getting 400 error for {city}, trying with minimal parameters")
#                         # Use only the limit parameter
#                         params = {"$limit": 100}
#                         response = await client.get(url, params=params)
            
#             response.raise_for_status()
#             data = response.json()
        
#         # If we got data with minimal parameters, log the first record to help with debugging
#         if data and len(data) > 0 and "$select" not in params:
#             print(f"Debug: First record from {city} with minimal parameters: {json.dumps(data[0], indent=2)}")
            
#             # Check if this looks like a 911 emergency calls dataset
#             first_record = data[0]
#             if not any(keyword in str(first_record).lower() for keyword in ["call", "emergency", "incident", "dispatch", "response"]):
#                 print(f"Warning: The dataset for {city} doesn't appear to be a 911 emergency calls dataset. Please verify the dataset ID.")
        
#         # Normalize all records
#         normalized_data = []
#         for record in data:
#             normalized_record = normalize_record(
#                 record, 
#                 city_config["field_mapping"], 
#                 city
#             )
#             normalized_data.append(normalized_record)
        
#         return normalized_data
    
#     except httpx.HTTPStatusError as e:
#         # Try to get more details from the response if available
#         error_details = ""
#         try:
#             error_details = e.response.text
#         except:
#             pass
        
#         raise httpx.HTTPStatusError(
#             f"Error fetching data from {city} API: {str(e)}. Details: {error_details}",
#             request=e.request,
#             response=e.response
#         )
#     except httpx.RequestError as e:
#         raise httpx.RequestError(f"Service unavailable: Could not connect to {city} API", request=e.request)
#     except json.JSONDecodeError as e:
#         raise ValueError(f"Error parsing response from {city} API: {str(e)}")
#     except Exception as e:
#         raise RuntimeError(f"Unexpected error: {str(e)}")

# async def fetch_federal_data(source: str, hours: int) -> List[Dict]:
#     """Fetch federal 911 data from a specified source"""
#     if source not in FEDERAL_REGISTRY:
#         raise ValueError(f"Federal source '{source}' is not supported")
    
#     source_config = FEDERAL_REGISTRY[source]
    
#     # Build the API URL
#     base_url = source_config["base_url"]
#     dataset_id = source_config["dataset_id"]
    
#     # Different APIs have different endpoint structures
#     if source == "data_gov_911":
#         # Data.gov uses CKAN API with a different endpoint structure
#         url = f"{base_url}{dataset_id}"
#     else:
#         url = f"{base_url}{dataset_id}.json"
    
#     # Start with default parameters
#     params = source_config.get("api_params", {}).copy()
    
#     # Add time filter if supported
#     if source_config.get("supports_soql", False):
#         try:
#             soql_filter = build_soql_filter("federal", source_config["date_field"], hours)
#             params["$where"] = soql_filter
#         except Exception as e:
#             print(f"Warning: Could not build SoQL filter for {source}: {str(e)}")
    
#     try:
#         # Fetch data from federal API
#         async with httpx.AsyncClient(timeout=APP_CONFIG["timeout"]) as client:
#             response = await client.get(url, params=params)
            
#             # If we get a 400 error, try without the SoQL filter
#             if response.status_code == 400 and source_config.get("supports_soql", False):
#                 print(f"Warning: Got 400 error for {source}, trying without SoQL filter")
#                 if "$where" in params:
#                     del params["$where"]
#                 response = await client.get(url, params=params)
            
#             response.raise_for_status()
            
#             # Handle different response formats
#             if source == "data_gov_911":
#                 # Data.gov returns results in a nested structure
#                 raw_data = response.json()
#                 data = raw_data.get("result", {}).get("results", [])
#             else:
#                 data = response.json()
        
#         # Normalize all records
#         normalized_data = []
#         for record in data:
#             normalized_record = normalize_record(
#                 record, 
#                 source_config["field_mapping"], 
#                 source
#             )
#             normalized_data.append(normalized_record)
        
#         return normalized_data
    
#     except httpx.HTTPStatusError as e:
#         error_details = ""
#         try:
#             error_details = e.response.text
#         except:
#             pass
        
#         raise httpx.HTTPStatusError(
#             f"Error fetching data from {source} API: {str(e)}. Details: {error_details}",
#             request=e.request,
#             response=e.response
#         )
#     except httpx.RequestError as e:
#         raise httpx.RequestError(f"Service unavailable: Could not connect to {source} API", request=e.request)
#     except json.JSONDecodeError as e:
#         raise ValueError(f"Error parsing response from {source} API: {str(e)}")
#     except Exception as e:
#         raise RuntimeError(f"Unexpected error: {str(e)}")
    



# ----------------------------------------test
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional
import httpx
import json
import re
from .config import CITY_REGISTRY, STATE_REGISTRY, FEDERAL_REGISTRY, APP_CONFIG

def build_soql_filter(city: str, date_field: str, hours: int) -> str:
    """Build SoQL filter for retrieving data from the last X hours"""
    start_time = datetime.utcnow() - timedelta(hours=hours)
    
    # Get city-specific date format if available
    city_config = CITY_REGISTRY.get(city, {})
    date_format = city_config.get("date_format")
    
    # Format the date according to city-specific requirements
    if date_format:
        date_str = start_time.strftime(date_format)
    else:
        # Default format with fractional seconds
        date_str = start_time.isoformat()
    
    return f"{date_field} >= '{date_str}'"

def set_nested_value(data_dict: Dict, keys: List[str], value: Any) -> None:
    """Set a value in a nested dictionary using dot notation keys"""
    if len(keys) == 1:
        data_dict[keys[0]] = value
    else:
        key = keys[0]
        if key not in data_dict:
            data_dict[key] = {}
        set_nested_value(data_dict[key], keys[1:], value)

def normalize_record(record: Dict, field_mapping: Dict, source: str) -> Dict:
    """Normalize a record to standard format"""
    normalized = {"source": source}
    
    # Apply field mapping
    for source_field, normalized_field in field_mapping.items():
        if source_field in record:
            # Handle nested fields using dot notation
            if "." in normalized_field:
                keys = normalized_field.split(".")
                set_nested_value(normalized, keys, record[source_field])
            else:
                normalized[normalized_field] = record[source_field]
    
    # Ensure required fields exist
    required_fields = ["timestamp", "incident_type"]
    for field in required_fields:
        if field not in normalized:
            normalized[field] = None if field == "timestamp" else "Unknown"
    
    # Add state and zipcode if available
    if source in CITY_REGISTRY:
        city_config = CITY_REGISTRY[source]
        if "state" in city_config:
            normalized["state"] = city_config["state"]
        if "zipcode" in city_config:
            normalized["zipcode"] = city_config["zipcode"]
    
    return normalized

async def fetch_city_data(city: str, hours: int) -> List[Dict]:
    """Fetch emergency call data from a city's API"""
    if city not in CITY_REGISTRY:
        raise ValueError(f"City '{city}' is not supported")
    
    city_config = CITY_REGISTRY[city]
    
    # Build the API URL
    base_url = city_config["base_url"]
    dataset_id = city_config["dataset_id"]
    url = f"{base_url}{dataset_id}.json"
    
    # Start with default parameters
    params = city_config.get("api_params", {}).copy()
    
    # Add SoQL filter if supported
    if city_config.get("supports_soql", False):
        try:
            soql_filter = build_soql_filter(city, city_config["date_field"], hours)
            params["$where"] = soql_filter
        except Exception as e:
            print(f"Warning: Could not build SoQL filter for {city}: {str(e)}")
    
    try:
        # Fetch data from city API
        async with httpx.AsyncClient(timeout=APP_CONFIG["timeout"]) as client:
            response = await client.get(url, params=params)
            
            # If we get a 400 error, try without the SoQL filter
            if response.status_code == 400:
                print(f"Warning: Got 400 error for {city}, trying without SoQL filter")
                if "$where" in params:
                    del params["$where"]
                response = await client.get(url, params=params)
                
                # If we still get a 400 error, try without the $select parameter
                if response.status_code == 400:
                    print(f"Warning: Still getting 400 error for {city}, trying without $select parameter")
                    if "$select" in params:
                        del params["$select"]
                    response = await client.get(url, params=params)
                    
                    # If we still get a 400 error, try with minimal parameters
                    if response.status_code == 400:
                        print(f"Warning: Still getting 400 error for {city}, trying with minimal parameters")
                        params = {"$limit": 100}
                        response = await client.get(url, params=params)
            
            response.raise_for_status()
            data = response.json()
        
        # Normalize all records
        normalized_data = []
        for record in data:
            normalized_record = normalize_record(
                record, 
                city_config["field_mapping"], 
                city
            )
            normalized_data.append(normalized_record)
        
        return normalized_data
    
    except httpx.HTTPStatusError as e:
        error_details = ""
        try:
            error_details = e.response.text
        except:
            pass
        
        raise httpx.HTTPStatusError(
            f"Error fetching data from {city} API: {str(e)}. Details: {error_details}",
            request=e.request,
            response=e.response
        )
    except httpx.RequestError as e:
        raise httpx.RequestError(f"Service unavailable: Could not connect to {city} API", request=e.request)
    except json.JSONDecodeError as e:
        raise ValueError(f"Error parsing response from {city} API: {str(e)}")
    except Exception as e:
        raise RuntimeError(f"Unexpected error: {str(e)}")

async def fetch_state_data(state: str, hours: int, city: Optional[str] = None, zipcode: Optional[str] = None) -> List[Dict]:
    """Fetch emergency call data for a state, optionally filtered by city or zipcode"""
    if state not in STATE_REGISTRY:
        raise ValueError(f"State '{state}' is not supported")
    
    state_config = STATE_REGISTRY[state]
    cities = state_config["cities"]
    
    # If a specific city is requested and it's in the state, fetch only that city
    if city and city in cities:
        city_data = await fetch_city_data(city, hours)
        
        # Filter by zipcode if provided
        if zipcode:
            # Extract zipcode from address if available
            filtered_data = []
            for record in city_data:
                # This is a simple implementation - in a real scenario, you would need
                # more sophisticated zipcode extraction and matching
                if "address" in record and record["address"]:
                    # Try to extract zipcode from address
                    match = re.search(r'\b\d{5}\b', record["address"])
                    if match and match.group() == zipcode:
                        filtered_data.append(record)
                elif "zipcode" in record and record["zipcode"] == zipcode:
                    filtered_data.append(record)
            city_data = filtered_data
        
        return city_data
    
    # Otherwise, fetch data for all cities in the state
    all_data = []
    for city_name in cities:
        try:
            city_data = await fetch_city_data(city_name, hours)
            all_data.extend(city_data)
        except Exception as e:
            print(f"Warning: Could not fetch data for {city_name}: {str(e)}")
    
    # Filter by zipcode if provided
    if zipcode:
        filtered_data = []
        for record in all_data:
            if "zipcode" in record and record["zipcode"] == zipcode:
                filtered_data.append(record)
        all_data = filtered_data
    
    return all_data

async def fetch_federal_data(source: str, hours: int, state: Optional[str] = None, city: Optional[str] = None, zipcode: Optional[str] = None) -> List[Dict]:
    """Fetch federal 911 data from a specified source, optionally filtered by state, city, or zipcode"""
    if source not in FEDERAL_REGISTRY:
        raise ValueError(f"Federal source '{source}' is not supported")
    
    source_config = FEDERAL_REGISTRY[source]
    
    # Build the API URL
    base_url = source_config["base_url"]
    dataset_id = source_config["dataset_id"]
    
    # Different APIs have different endpoint structures
    if source == "data_gov_911":
        # Data.gov uses CKAN API with a different endpoint structure
        url = f"{base_url}{dataset_id}"
    else:
        url = f"{base_url}{dataset_id}.json"
    
    # Start with default parameters
    params = source_config.get("api_params", {}).copy()
    
    try:
        # Fetch data from federal API
        async with httpx.AsyncClient(timeout=APP_CONFIG["timeout"]) as client:
            response = await client.get(url, params=params)
            response.raise_for_status()
            
            # Handle different response formats
            if source == "data_gov_911":
                # Data.gov returns results in a nested structure
                raw_data = response.json()
                data = raw_data.get("result", {}).get("results", [])
            else:
                data = response.json()
        
        # Normalize all records
        normalized_data = []
        for record in data:
            normalized_record = normalize_record(
                record, 
                source_config["field_mapping"], 
                source
            )
            normalized_data.append(normalized_record)
        
        # Filter by state, city, or zipcode if provided
        if state or city or zipcode:
            filtered_data = []
            for record in normalized_data:
                include = True
                
                if state and record.get("state") != state:
                    include = False
                
                if city and record.get("city") != city:
                    include = False
                
                if zipcode and record.get("zipcode") != zipcode:
                    include = False
                
                if include:
                    filtered_data.append(record)
            
            normalized_data = filtered_data
        
        return normalized_data
    
    except httpx.HTTPStatusError as e:
        error_details = ""
        try:
            error_details = e.response.text
        except:
            pass
        
        raise httpx.HTTPStatusError(
            f"Error fetching data from {source} API: {str(e)}. Details: {error_details}",
            request=e.request,
            response=e.response
        )
    except httpx.RequestError as e:
        raise httpx.RequestError(f"Service unavailable: Could not connect to {source} API", request=e.request)
    except json.JSONDecodeError as e:
        raise ValueError(f"Error parsing response from {source} API: {str(e)}")
    except Exception as e:
        raise RuntimeError(f"Unexpected error: {str(e)}")