# from typing import Dict, Any

# # City registry configuration
# CITY_REGISTRY: Dict[str, Dict[str, Any]] = {
#     "san_francisco": {
#         "base_url": "https://data.sfgov.org/resource/",
#         "dataset_id": "gnap-fj3t",
#         "date_field": "received_datetime",
#         "date_format": None,  # Use default ISO format
#         "field_mapping": {
#             "received_datetime": "timestamp",
#             "call_type_final_desc": "incident_type",
#             "cad_number": "call_id",
#             "priority_final": "priority",
#             "agency": "agency",
#             "disposition": "disposition",
#             "onview_flag": "onview_flag",
#             "sensitive_call": "sensitive_call",
#             "entry_datetime": "entry_time",
#             "dispatch_datetime": "dispatch_time",
#             "enroute_datetime": "enroute_time",
#             "onscene_datetime": "onscene_time",
#             "close_datetime": "close_time",
#             "call_type_original": "call_type_original",
#             "call_type_original_desc": "call_type_original_desc",
#             "call_type_final": "call_type_final",
#             "priority_original": "priority_original"
#         },
#         "supports_soql": True,
#         "api_params": {
#             "$limit": 1000
#         }
#     },
#     "new_york": {
#         "base_url": "https://data.cityofnewyork.us/resource/",
#         "dataset_id": "8sjn-2jm8",  # Current calls (not historic)
#         "date_field": "created_date",
#         "date_format": "%Y-%m-%dT%H:%M:%S",  # Format without fractional seconds
#         "field_mapping": {
#             "created_date": "timestamp",
#             "call_type": "incident_type",
#             "incident_key": "call_id",
#             "typ_desc": "incident_type_description",
#             "nypd_pct_cd": "police_precinct",
#             "boro_nm": "borough",
#             "add_ts": "call_added_time",
#             "disp_ts": "dispatch_time",
#             "arrivd_ts": "arrival_time",
#             "closng_ts": "close_time",
#             "latitude": "latitude",
#             "longitude": "longitude",
#             "location": "location"
#         },
#         "supports_soql": True,
#         "api_params": {
#             "$limit": 1000
#         }
#     },
#     "chicago": {
#         "base_url": "https://data.cityofchicago.org/resource/",
#         "dataset_id": "ijzp-q8t2",  # Chicago Crimes dataset (includes recent 911 calls)
#         "date_field": "date",
#         "date_format": "%Y-%m-%dT%H:%M:%S",  # Format without fractional seconds
#         "field_mapping": {
#             "date": "timestamp",
#             "primary_type": "incident_type",
#             "case_number": "call_id",
#             "district": "district",
#             "location_description": "location_desc",
#             "block": "address",
#             "beat": "beat",
#             "ward": "ward",
#             "community_area": "community_area"
#         },
#         "supports_soql": True,
#         "api_params": {
#             "$limit": 1000
#         }
#     },
#     "seattle": {
#         "base_url": "https://data.seattle.gov/resource/",
#         "dataset_id": "kzjm-xkqj",  # Seattle 911 Incident Response
#         "date_field": "datetime",
#         "date_format": "%Y-%m-%dT%H:%M:%S",
#         "field_mapping": {
#             "datetime": "timestamp",
#             "event_clearance_description": "incident_type",
#             "hundred_block_location": "address",
#             "precinct": "precinct",
#             "sector": "sector",
#             "beat": "beat",
#             "initial_type": "initial_type",
#             "final_type": "final_type"
#         },
#         "supports_soql": True,
#         "api_params": {
#             "$limit": 1000
#         }
#     },
#     "baltimore": {
#         "base_url": "https://data.baltimorecity.gov/resource/",
#         "dataset_id": "3i3v-ibrt",  # Baltimore 911 Calls
#         "date_field": "callDateTime",
#         "date_format": "%Y-%m-%dT%H:%M:%S",
#         "field_mapping": {
#             "callDateTime": "timestamp",
#             "type": "incident_type",
#             "description": "description",
#             "location": "location",
#             "district": "district",
#             "neighborhood": "neighborhood",
#             "policeDistrict": "police_district"
#         },
#         "supports_soql": True,
#         "api_params": {
#             "$limit": 1000
#         }
#     },
#     "dallas": {
#         "base_url": "https://www.dallasopendata.com/resource/",
#         "dataset_id": "qb4t-a3a7",  # Dallas 911 Calls
#         "date_field": "call_date_time",
#         "date_format": "%Y-%m-%dT%H:%M:%S",
#         "field_mapping": {
#             "call_date_time": "timestamp",
#             "call_type": "incident_type",
#             "problem": "problem",
#             "location": "location",
#             "address": "address",
#             "division": "division",
#             "sector": "sector"
#         },
#         "supports_soql": True,
#         "api_params": {
#             "$limit": 1000
#         }
#     },
#     "detroit": {
#         "base_url": "https://data.detroitmi.gov/resource/",
#         "dataset_id": "9i5z-3j5m",  # Detroit 911 Calls
#         "date_field": "calldatetime",
#         "date_format": "%Y-%m-%dT%H:%M:%S",
#         "field_mapping": {
#             "calldatetime": "timestamp",
#             "calltype": "incident_type",
#             "natureofcall": "nature_of_call",
#             "location": "location",
#             "address": "address",
#             "precinct": "precinct"
#         },
#         "supports_soql": True,
#         "api_params": {
#             "$limit": 1000
#         }
#     },
#     "washington_dc": {
#         "base_url": "https://opendata.dc.gov/resource/",
#         "dataset_id": "ucnv-2v3w",  # DC 911 Calls
#         "date_field": "call_date",
#         "date_format": "%Y-%m-%dT%H:%M:%S",
#         "field_mapping": {
#             "call_date": "timestamp",
#             "call_type": "incident_type",
#             "method": "method",
#             "location": "location",
#             "address": "address",
#             "ward": "ward",
#             "district": "district"
#         },
#         "supports_soql": True,
#         "api_params": {
#             "$limit": 1000
#         }
#     },
#     "austin": {
#         "base_url": "https://data.austintexas.gov/resource/",
#         "dataset_id": "i6jg-9mnd",  # Austin 911 Calls
#         "date_field": "create_time_incident",
#         "date_format": "%Y-%m-%dT%H:%M:%S",
#         "field_mapping": {
#             "create_time_incident": "timestamp",
#             "type_description": "incident_type",
#             "primary_key": "call_id",
#             "location": "location",
#             "address": "address",
#             "sector": "sector",
#             "district": "district"
#         },
#         "supports_soql": True,
#         "api_params": {
#             "$limit": 1000
#         }
#     },
#     "phoenix": {
#         "base_url": "https://data.phoenixopendata.com/resource/",
#         "dataset_id": "urua-mdai",  # Phoenix 911 Calls
#         "date_field": "callreceived",
#         "date_format": "%Y-%m-%dT%H:%M:%S",
#         "field_mapping": {
#             "callreceived": "timestamp",
#             "calltype": "incident_type",
#             "calldisposition": "disposition",
#             "location": "location",
#             "address": "address",
#             "precinct": "precinct",
#             "beat": "beat"
#         },
#         "supports_soql": True,
#         "api_params": {
#             "$limit": 1000
#         }
#     }
# }

# # Application configuration
# APP_CONFIG = {
#     "default_hours": 24,  # Default hours to look back
#     "max_hours": 168,     # Maximum hours to look back (1 week)
#     "timeout": 30.0       # Request timeout in seconds
# }





# ================================================


# federal level test




# from typing import Dict, Any

# # City registry configuration
# CITY_REGISTRY: Dict[str, Dict[str, Any]] = {
#     "san_francisco": {
#         "base_url": "https://data.sfgov.org/resource/",
#         "dataset_id": "gnap-fj3t",
#         "date_field": "received_datetime",
#         "date_format": None,  # Use default ISO format
#         "field_mapping": {
#             "received_datetime": "timestamp",
#             "call_type_final_desc": "incident_type",
#             "cad_number": "call_id",
#             "priority_final": "priority",
#             "agency": "agency",
#             "disposition": "disposition",
#             "onview_flag": "onview_flag",
#             "sensitive_call": "sensitive_call",
#             "entry_datetime": "entry_time",
#             "dispatch_datetime": "dispatch_time",
#             "enroute_datetime": "enroute_time",
#             "onscene_datetime": "onscene_time",
#             "close_datetime": "close_time",
#             "call_type_original": "call_type_original",
#             "call_type_original_desc": "call_type_original_desc",
#             "call_type_final": "call_type_final",
#             "priority_original": "priority_original"
#         },
#         "supports_soql": True,
#         "api_params": {
#             "$limit": 1000
#         }
#     },
#     "new_york": {
#         "base_url": "https://data.cityofnewyork.us/resource/",
#         "dataset_id": "8sjn-2jm8",  # Current calls (not historic)
#         "date_field": "created_date",
#         "date_format": "%Y-%m-%dT%H:%M:%S",  # Format without fractional seconds
#         "field_mapping": {
#             "created_date": "timestamp",
#             "call_type": "incident_type",
#             "incident_key": "call_id",
#             "typ_desc": "incident_type_description",
#             "nypd_pct_cd": "police_precinct",
#             "boro_nm": "borough",
#             "add_ts": "call_added_time",
#             "disp_ts": "dispatch_time",
#             "arrivd_ts": "arrival_time",
#             "closng_ts": "close_time",
#             "latitude": "latitude",
#             "longitude": "longitude",
#             "location": "location"
#         },
#         "supports_soql": True,
#         "api_params": {
#             "$limit": 1000
#         }
#     },
#     "chicago": {
#         "base_url": "https://data.cityofchicago.org/resource/",
#         "dataset_id": "ijzp-q8t2",  # Chicago Crimes dataset (includes recent 911 calls)
#         "date_field": "date",
#         "date_format": "%Y-%m-%dT%H:%M:%S",  # Format without fractional seconds
#         "field_mapping": {
#             "date": "timestamp",
#             "primary_type": "incident_type",
#             "case_number": "call_id",
#             "district": "district",
#             "location_description": "location_desc",
#             "block": "address",
#             "beat": "beat",
#             "ward": "ward",
#             "community_area": "community_area"
#         },
#         "supports_soql": True,
#         "api_params": {
#             "$limit": 1000
#         }
#     },
#     "seattle": {
#         "base_url": "https://data.seattle.gov/resource/",
#         "dataset_id": "kzjm-xkqj",  # Seattle 911 Incident Response
#         "date_field": "datetime",
#         "date_format": "%Y-%m-%dT%H:%M:%S",
#         "field_mapping": {
#             "datetime": "timestamp",
#             "event_clearance_description": "incident_type",
#             "hundred_block_location": "address",
#             "precinct": "precinct",
#             "sector": "sector",
#             "beat": "beat",
#             "initial_type": "initial_type",
#             "final_type": "final_type"
#         },
#         "supports_soql": True,
#         "api_params": {
#             "$limit": 1000
#         }
#     },
#     "baltimore": {
#         "base_url": "https://data.baltimorecity.gov/resource/",
#         "dataset_id": "3i3v-ibrt",  # Baltimore 911 Calls
#         "date_field": "callDateTime",
#         "date_format": "%Y-%m-%dT%H:%M:%S",
#         "field_mapping": {
#             "callDateTime": "timestamp",
#             "type": "incident_type",
#             "description": "description",
#             "location": "location",
#             "district": "district",
#             "neighborhood": "neighborhood",
#             "policeDistrict": "police_district"
#         },
#         "supports_soql": True,
#         "api_params": {
#             "$limit": 1000
#         }
#     },
#     "dallas": {
#         "base_url": "https://www.dallasopendata.com/resource/",
#         "dataset_id": "qb4t-a3a7",  # Dallas 911 Calls
#         "date_field": "call_date_time",
#         "date_format": "%Y-%m-%dT%H:%M:%S",
#         "field_mapping": {
#             "call_date_time": "timestamp",
#             "call_type": "incident_type",
#             "problem": "problem",
#             "location": "location",
#             "address": "address",
#             "division": "division",
#             "sector": "sector"
#         },
#         "supports_soql": True,
#         "api_params": {
#             "$limit": 1000
#         }
#     },
#     "detroit": {
#         "base_url": "https://data.detroitmi.gov/resource/",
#         "dataset_id": "9i5z-3j5m",  # Detroit 911 Calls
#         "date_field": "calldatetime",
#         "date_format": "%Y-%m-%dT%H:%M:%S",
#         "field_mapping": {
#             "calldatetime": "timestamp",
#             "calltype": "incident_type",
#             "natureofcall": "nature_of_call",
#             "location": "location",
#             "address": "address",
#             "precinct": "precinct"
#         },
#         "supports_soql": True,
#         "api_params": {
#             "$limit": 1000
#         }
#     },
#     "washington_dc": {
#         "base_url": "https://opendata.dc.gov/resource/",
#         "dataset_id": "ucnv-2v3w",  # DC 911 Calls
#         "date_field": "call_date",
#         "date_format": "%Y-%m-%dT%H:%M:%S",
#         "field_mapping": {
#             "call_date": "timestamp",
#             "call_type": "incident_type",
#             "method": "method",
#             "location": "location",
#             "address": "address",
#             "ward": "ward",
#             "district": "district"
#         },
#         "supports_soql": True,
#         "api_params": {
#             "$limit": 1000
#         }
#     },
#     "austin": {
#         "base_url": "https://data.austintexas.gov/resource/",
#         "dataset_id": "i6jg-9mnd",  # Austin 911 Calls
#         "date_field": "create_time_incident",
#         "date_format": "%Y-%m-%dT%H:%M:%S",
#         "field_mapping": {
#             "create_time_incident": "timestamp",
#             "type_description": "incident_type",
#             "primary_key": "call_id",
#             "location": "location",
#             "address": "address",
#             "sector": "sector",
#             "district": "district"
#         },
#         "supports_soql": True,
#         "api_params": {
#             "$limit": 1000
#         }
#     },
#     "phoenix": {
#         "base_url": "https://data.phoenixopendata.com/resource/",
#         "dataset_id": "urua-mdai",  # Phoenix 911 Calls
#         "date_field": "callreceived",
#         "date_format": "%Y-%m-%dT%H:%M:%S",
#         "field_mapping": {
#             "callreceived": "timestamp",
#             "calltype": "incident_type",
#             "calldisposition": "disposition",
#             "location": "location",
#             "address": "address",
#             "precinct": "precinct",
#             "beat": "beat"
#         },
#         "supports_soql": True,
#         "api_params": {
#             "$limit": 1000
#         }
#     }
# }

# # Federal registry configuration
# FEDERAL_REGISTRY: Dict[str, Dict[str, Any]] = {
#     "fcc_psap_registry": {
#         "name": "FCC Master PSAP Registry",
#         "base_url": "https://opendata.fcc.gov/resource/",
#         "dataset_id": "b7k6-2b9w",  # Placeholder ID - replace with actual
#         "description": "Complete database of all Public Safety Answering Points",
#         "date_field": "last_updated",
#         "date_format": "%Y-%m-%dT%H:%M:%S",
#         "field_mapping": {
#             "psap_id": "psap_id",
#             "psap_name": "name",
#             "state": "state",
#             "county": "county",
#             "city": "city",
#             "last_updated": "last_updated",
#             "latitude": "latitude",
#             "longitude": "longitude"
#         },
#         "supports_soql": True,
#         "api_params": {
#             "$limit": 1000
#         }
#     },
#     "data_gov_911": {
#         "name": "Data.gov 911 Datasets",
#         "base_url": "https://catalog.data.gov/api/3/action/",
#         "dataset_id": "package_search",
#         "description": "Federal catalog of 911 datasets across jurisdictions",
#         "date_field": "metadata_created",
#         "date_format": "%Y-%m-%dT%H:%M:%S",
#         "field_mapping": {
#             "id": "dataset_id",
#             "title": "title",
#             "notes": "description",
#             "metadata_created": "created_date",
#             "metadata_modified": "modified_date",
#             "author": "author",
#             "author_email": "author_email",
#             "state": "state"
#         },
#         "supports_soql": False,  # Data.gov uses CKAN API, not SoQL
#         "api_params": {
#             "rows": 1000,
#             "q": "911 emergency"
#         }
#     },
#     "nine_one_one_gov": {
#         "name": "911.gov National Statistics",
#         "base_url": "https://www.911.gov/api/",
#         "dataset_id": "statistics",
#         "description": "National statistics and data resources",
#         "date_field": "date",
#         "date_format": "%Y-%m-%d",
#         "field_mapping": {
#             "date": "date",
#             "state": "state",
#             "call_volume": "call_volume",
#             "response_time": "response_time",
#             "abandoned_calls": "abandoned_calls"
#         },
#         "supports_soql": False,
#         "api_params": {
#             "format": "json"
#         }
#     }
# }

# # Application configuration
# APP_CONFIG = {
#     "default_hours": 24,  # Default hours to look back
#     "max_hours": 168,     # Maximum hours to look back (1 week)
#     "timeout": 30.0       # Request timeout in seconds
# }


# -----------------------------------------test



from typing import Dict, Any, List, Optional

# City registry configuration - only including verified working cities
CITY_REGISTRY: Dict[str, Dict[str, Any]] = {
    "san_francisco": {
        "base_url": "https://data.sfgov.org/resource/",
        "dataset_id": "gnap-fj3t",
        "date_field": "received_datetime",
        "date_format": None,
        "field_mapping": {
            "received_datetime": "timestamp",
            "call_type_final_desc": "incident_type",
            "cad_number": "call_id",
            "priority_final": "priority",
            "agency": "agency",
            "disposition": "disposition",
            "onview_flag": "onview_flag",
            "sensitive_call": "sensitive_call",
            "entry_datetime": "entry_time",
            "dispatch_datetime": "dispatch_time",
            "enroute_datetime": "enroute_time",
            "onscene_datetime": "onscene_time",
            "close_datetime": "close_time",
            "call_type_original": "call_type_original",
            "call_type_original_desc": "call_type_original_desc",
            "call_type_final": "call_type_final",
            "priority_original": "priority_original"
        },
        "supports_soql": True,
        "api_params": {
            "$limit": 1000
        },
        "state": "CA",
        "zipcode": None
    },
    "chicago": {
        "base_url": "https://data.cityofchicago.org/resource/",
        "dataset_id": "ijzp-q8t2",
        "date_field": "date",
        "date_format": "%Y-%m-%dT%H:%M:%S",
        "field_mapping": {
            "date": "timestamp",
            "primary_type": "incident_type",
            "case_number": "call_id",
            "district": "district",
            "location_description": "location_desc",
            "block": "address",
            "beat": "beat",
            "ward": "ward",
            "community_area": "community_area"
        },
        "supports_soql": True,
        "api_params": {
            "$limit": 1000
        },
        "state": "IL",
        "zipcode": None
    },
    "seattle": {
        "base_url": "https://data.seattle.gov/resource/",
        "dataset_id": "kzjm-xkqj",
        "date_field": "datetime",
        "date_format": "%Y-%m-%dT%H:%M:%S",
        "field_mapping": {
            "datetime": "timestamp",
            "event_clearance_description": "incident_type",
            "hundred_block_location": "address",
            "precinct": "precinct",
            "sector": "sector",
            "beat": "beat",
            "initial_type": "initial_type",
            "final_type": "final_type"
        },
        "supports_soql": True,
        "api_params": {
            "$limit": 1000
        },
        "state": "WA",
        "zipcode": None
    }
}

# State registry configuration - groups cities by state
STATE_REGISTRY: Dict[str, Dict[str, Any]] = {
    "CA": {
        "name": "California",
        "cities": ["san_francisco"],
        "filters": ["state", "city", "zipcode"]
    },
    "IL": {
        "name": "Illinois",
        "cities": ["chicago"],
        "filters": ["state", "city", "zipcode"]
    },
    "WA": {
        "name": "Washington",
        "cities": ["seattle"],
        "filters": ["state", "city", "zipcode"]
    }
}

# Federal registry configuration - only including verified working sources
FEDERAL_REGISTRY: Dict[str, Dict[str, Any]] = {
    "data_gov_911": {
        "name": "Data.gov 911 Datasets",
        "base_url": "https://catalog.data.gov/api/3/action/",
        "dataset_id": "package_search",
        "description": "Federal catalog of 911 datasets across jurisdictions",
        "date_field": "metadata_created",
        "date_format": "%Y-%m-%dT%H:%M:%S",
        "field_mapping": {
            "id": "dataset_id",
            "title": "title",
            "notes": "description",
            "metadata_created": "created_date",
            "metadata_modified": "modified_date",
            "author": "author",
            "author_email": "author_email",
            "state": "state"
        },
        "supports_soql": False,
        "api_params": {
            "rows": 1000,
            "q": "911 emergency"
        },
        "filters": ["state", "city", "zipcode"]
    }
}

# Application configuration
APP_CONFIG = {
    "default_hours": 24,
    "max_hours": 168,
    "timeout": 30.0
}