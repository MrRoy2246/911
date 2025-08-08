# from fastapi import FastAPI, HTTPException, Query, Depends
# from fastapi.responses import JSONResponse
# from datetime import datetime
# from typing import List, Dict, Any
# import httpx
# import logging

# from app.config import CITY_REGISTRY, APP_CONFIG
# from app.services import fetch_city_data

# # Configure logging
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

# # Create FastAPI app
# app = FastAPI(
#     title="911 Emergency Call Data API",
#     description="API for fetching 911 emergency call data from multiple cities",
#     version="1.0.0"
# )

# # Dependency to validate hours parameter
# async def validate_hours(hours: int = Query(..., ge=1, le=APP_CONFIG["max_hours"])):
#     """Validate the hours parameter"""
#     if hours > APP_CONFIG["max_hours"]:
#         raise HTTPException(
#             status_code=400,
#             detail=f"Hours cannot exceed {APP_CONFIG['max_hours']} (1 week)"
#         )
#     return hours

# @app.get("/data", response_model=List[Dict[str, Any]])
# async def get_emergency_calls(
#     city: str = Query(..., description="City name (e.g., san_francisco)"),
#     hours: int = Query(APP_CONFIG["default_hours"], description="Number of hours to look back"),
#     validated_hours: int = Depends(validate_hours)
# ):
#     """
#     Fetch 911 emergency call data for a specific city from the last X hours.
    
#     Args:
#         city: The name of the city (must be in the registry)
#         hours: Number of hours to look back (default: 24)
    
#     Returns:
#         List of normalized emergency call records
#     """
#     try:
#         # Use validated hours
#         hours_to_fetch = validated_hours
        
#         # Fetch data from city API
#         data = await fetch_city_data(city, hours_to_fetch)
#         return data
    
#     except ValueError as e:
#         raise HTTPException(status_code=404, detail=str(e))
#     except httpx.HTTPStatusError as e:
#         raise HTTPException(
#             status_code=e.response.status_code,
#             detail=str(e)
#         )
#     except httpx.RequestError as e:
#         raise HTTPException(
#             status_code=503,
#             detail=str(e)
#         )
#     except (ValueError, RuntimeError) as e:
#         raise HTTPException(
#             status_code=500,
#             detail=str(e)
#         )
#     except Exception as e:
#         logger.error(f"Unexpected error: {str(e)}")
#         raise HTTPException(
#             status_code=500,
#             detail="An unexpected error occurred"
#         )

# @app.get("/health")
# async def health_check():
#     """Health check endpoint"""
#     return {"status": "healthy", "timestamp": datetime.utcnow().isoformat()}

# @app.get("/")
# async def root():
#     """Root endpoint with API documentation"""
#     return {
#         "message": "911 Emergency Call Data API",
#         "version": "1.0.0",
#         "endpoints": {
#             "data": "/data?city=<city_name>&hours=<hours>",
#             "health": "/health"
#         },
#         "supported_cities": list(CITY_REGISTRY.keys()),
#         "configuration": {
#             "default_hours": APP_CONFIG["default_hours"],
#             "max_hours": APP_CONFIG["max_hours"]
#         }
#     }

# @app.get("/cities")
# async def list_cities():
#     """List all supported cities"""
#     cities_info = {}
#     for city, config in CITY_REGISTRY.items():
#         cities_info[city] = {
#             "base_url": config["base_url"],
#             "dataset_id": config["dataset_id"],
#             "supports_soql": config["supports_soql"]
#         }
#     return {"supported_cities": cities_info}
# # Add this to your existing main.py

# @app.get("/federal-data", response_model=List[Dict[str, Any]])
# async def get_federal_data(
#     source: str = Query(..., description="Federal data source (e.g., fcc_psap_registry, data_gov_911, nine_one_one_gov)"),
#     hours: int = Query(APP_CONFIG["default_hours"], description="Number of hours to look back"),
#     validated_hours: int = Depends(validate_hours)
# ):
#     """
#     Fetch federal 911 emergency call data from a specified source.
    
#     Args:
#         source: The name of the federal data source
#         hours: Number of hours to look back (default: 24)
    
#     Returns:
#         List of normalized federal data records
#     """
#     try:
#         # Use validated hours
#         hours_to_fetch = validated_hours
        
#         # Fetch data from federal API
#         data = await fetch_federal_data(source, hours_to_fetch)
#         return data
    
#     except ValueError as e:
#         raise HTTPException(status_code=404, detail=str(e))
#     except httpx.HTTPStatusError as e:
#         raise HTTPException(
#             status_code=e.response.status_code,
#             detail=str(e)
#         )
#     except httpx.RequestError as e:
#         raise HTTPException(
#             status_code=503,
#             detail=str(e)
#         )
#     except (ValueError, RuntimeError) as e:
#         raise HTTPException(
#             status_code=500,
#             detail=str(e)
#         )
#     except Exception as e:
#         logger.error(f"Unexpected error: {str(e)}")
#         raise HTTPException(
#             status_code=500,
#             detail="An unexpected error occurred"
#         )

# @app.get("/federal-sources")
# async def list_federal_sources():
#     """List all supported federal data sources"""
#     sources_info = {}
#     for source, config in FEDERAL_REGISTRY.items():
#         sources_info[source] = {
#             "name": config["name"],
#             "description": config["description"],
#             "supports_soql": config["supports_soql"]
#         }
#     return {"federal_sources": sources_info}

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)

# ============================================================

# federal test


# from fastapi import FastAPI, HTTPException, Query, Depends
# from fastapi.responses import JSONResponse
# from datetime import datetime
# from typing import List, Dict, Any
# import httpx
# import logging

# from .config import CITY_REGISTRY, FEDERAL_REGISTRY, APP_CONFIG
# from .services import fetch_city_data, fetch_federal_data

# # Configure logging
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

# # Create FastAPI app
# app = FastAPI(
#     title="911 Emergency Call Data API",
#     description="API for fetching 911 emergency call data from multiple cities and federal sources",
#     version="1.0.0"
# )

# # Dependency to validate hours parameter
# async def validate_hours(hours: int = Query(..., ge=1, le=APP_CONFIG["max_hours"])):
#     """Validate the hours parameter"""
#     if hours > APP_CONFIG["max_hours"]:
#         raise HTTPException(
#             status_code=400,
#             detail=f"Hours cannot exceed {APP_CONFIG['max_hours']} (1 week)"
#         )
#     return hours

# @app.get("/data", response_model=List[Dict[str, Any]])
# async def get_emergency_calls(
#     city: str = Query(..., description="City name (e.g., san_francisco)"),
#     hours: int = Query(APP_CONFIG["default_hours"], description="Number of hours to look back"),
#     validated_hours: int = Depends(validate_hours)
# ):
#     """
#     Fetch 911 emergency call data for a specific city from the last X hours.
    
#     Args:
#         city: The name of the city (must be in the registry)
#         hours: Number of hours to look back (default: 24)
    
#     Returns:
#         List of normalized emergency call records
#     """
#     try:
#         # Use validated hours
#         hours_to_fetch = validated_hours
        
#         # Fetch data from city API
#         data = await fetch_city_data(city, hours_to_fetch)
#         return data
    
#     except ValueError as e:
#         raise HTTPException(status_code=404, detail=str(e))
#     except httpx.HTTPStatusError as e:
#         raise HTTPException(
#             status_code=e.response.status_code,
#             detail=str(e)
#         )
#     except httpx.RequestError as e:
#         raise HTTPException(
#             status_code=503,
#             detail=str(e)
#         )
#     except (ValueError, RuntimeError) as e:
#         raise HTTPException(
#             status_code=500,
#             detail=str(e)
#         )
#     except Exception as e:
#         logger.error(f"Unexpected error: {str(e)}")
#         raise HTTPException(
#             status_code=500,
#             detail="An unexpected error occurred"
#         )

# @app.get("/federal-data", response_model=List[Dict[str, Any]])
# async def get_federal_data(
#     source: str = Query(..., description="Federal data source (e.g., fcc_psap_registry, data_gov_911, nine_one_one_gov)"),
#     hours: int = Query(APP_CONFIG["default_hours"], description="Number of hours to look back"),
#     validated_hours: int = Depends(validate_hours)
# ):
#     """
#     Fetch federal 911 emergency call data from a specified source.
    
#     Args:
#         source: The name of the federal data source
#         hours: Number of hours to look back (default: 24)
    
#     Returns:
#         List of normalized federal data records
#     """
#     try:
#         # Use validated hours
#         hours_to_fetch = validated_hours
        
#         # Fetch data from federal API
#         data = await fetch_federal_data(source, hours_to_fetch)
#         return data
    
#     except ValueError as e:
#         raise HTTPException(status_code=404, detail=str(e))
#     except httpx.HTTPStatusError as e:
#         raise HTTPException(
#             status_code=e.response.status_code,
#             detail=str(e)
#         )
#     except httpx.RequestError as e:
#         raise HTTPException(
#             status_code=503,
#             detail=str(e)
#         )
#     except (ValueError, RuntimeError) as e:
#         raise HTTPException(
#             status_code=500,
#             detail=str(e)
#         )
#     except Exception as e:
#         logger.error(f"Unexpected error: {str(e)}")
#         raise HTTPException(
#             status_code=500,
#             detail="An unexpected error occurred"
#         )

# @app.get("/health")
# async def health_check():
#     """Health check endpoint"""
#     return {"status": "healthy", "timestamp": datetime.utcnow().isoformat()}

# @app.get("/cities")
# async def list_cities():
#     """List all supported cities"""
#     cities_info = {}
#     for city, config in CITY_REGISTRY.items():
#         cities_info[city] = {
#             "base_url": config["base_url"],
#             "dataset_id": config["dataset_id"],
#             "supports_soql": config["supports_soql"]
#         }
#     return {"supported_cities": cities_info}

# @app.get("/federal-sources")
# async def list_federal_sources():
#     """List all supported federal data sources"""
#     sources_info = {}
#     for source, config in FEDERAL_REGISTRY.items():
#         sources_info[source] = {
#             "name": config["name"],
#             "description": config["description"],
#             "supports_soql": config["supports_soql"]
#         }
#     return {"federal_sources": sources_info}

# @app.get("/")
# async def root():
#     """Root endpoint with API documentation"""
#     return {
#         "message": "911 Emergency Call Data API",
#         "version": "1.0.0",
#         "endpoints": {
#             "data": "/data?city=<city_name>&hours=<hours>",
#             "federal-data": "/federal-data?source=<source_name>&hours=<hours>",
#             "health": "/health",
#             "cities": "/cities",
#             "federal-sources": "/federal-sources"
#         }
#     }

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)




# ------------------------------------------test
from fastapi import FastAPI, HTTPException, Query, Depends
from fastapi.responses import JSONResponse
from datetime import datetime
from typing import List, Dict, Any, Optional
import httpx
import logging

from .config import CITY_REGISTRY, STATE_REGISTRY, FEDERAL_REGISTRY, APP_CONFIG
from .services import fetch_city_data, fetch_state_data, fetch_federal_data
from .models import EmergencyCallResponse

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create FastAPI app
app = FastAPI(
    title="911 Emergency Call Data API",
    description="API for fetching 911 emergency call data from multiple cities, states, and federal sources",
    version="1.0.0"
)

# Dependency to validate hours parameter
async def validate_hours(hours: int = Query(..., ge=1, le=APP_CONFIG["max_hours"])):
    """Validate the hours parameter"""
    if hours > APP_CONFIG["max_hours"]:
        raise HTTPException(
            status_code=400,
            detail=f"Hours cannot exceed {APP_CONFIG['max_hours']} (1 week)"
        )
    return hours

@app.get("/data", response_model=EmergencyCallResponse)
async def get_emergency_calls(
    city: str = Query(..., description="City name (e.g., san_francisco)"),
    hours: int = Query(APP_CONFIG["default_hours"], description="Number of hours to look back"),
    validated_hours: int = Depends(validate_hours)
):
    """
    Fetch 911 emergency call data for a specific city from the last X hours.
    
    Args:
        city: The name of the city (must be in the registry)
        hours: Number of hours to look back (default: 24)
    
    Returns:
        EmergencyCallResponse with count and data
    """
    try:
        # Use validated hours
        hours_to_fetch = validated_hours
        
        # Fetch data from city API
        data = await fetch_city_data(city, hours_to_fetch)
        
        return EmergencyCallResponse(
            count=len(data),
            data=data
        )
    
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except httpx.HTTPStatusError as e:
        raise HTTPException(
            status_code=e.response.status_code,
            detail=str(e)
        )
    except httpx.RequestError as e:
        raise HTTPException(
            status_code=503,
            detail=str(e)
        )
    except (ValueError, RuntimeError) as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail="An unexpected error occurred"
        )

@app.get("/state-data", response_model=EmergencyCallResponse)
async def get_state_data(
    state: str = Query(..., description="State code (e.g., CA, IL, WA)"),
    hours: int = Query(APP_CONFIG["default_hours"], description="Number of hours to look back"),
    city: Optional[str] = Query(None, description="Optional city name to filter within the state"),
    zipcode: Optional[str] = Query(None, description="Optional zipcode to filter within the state"),
    validated_hours: int = Depends(validate_hours)
):
    """
    Fetch 911 emergency call data for a specific state, optionally filtered by city or zipcode.
    
    Args:
        state: The state code (must be in the registry)
        hours: Number of hours to look back (default: 24)
        city: Optional city name to filter within the state
        zipcode: Optional zipcode to filter within the state
    
    Returns:
        EmergencyCallResponse with count and data
    """
    try:
        # Use validated hours
        hours_to_fetch = validated_hours
        
        # Fetch data from state APIs
        data = await fetch_state_data(state, hours_to_fetch, city, zipcode)
        
        return EmergencyCallResponse(
            count=len(data),
            data=data
        )
    
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except httpx.HTTPStatusError as e:
        raise HTTPException(
            status_code=e.response.status_code,
            detail=str(e)
        )
    except httpx.RequestError as e:
        raise HTTPException(
            status_code=503,
            detail=str(e)
        )
    except (ValueError, RuntimeError) as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail="An unexpected error occurred"
        )

@app.get("/federal-data", response_model=EmergencyCallResponse)
async def get_federal_data(
    source: str = Query(..., description="Federal data source (e.g., data_gov_911)"),
    hours: int = Query(APP_CONFIG["default_hours"], description="Number of hours to look back"),
    state: Optional[str] = Query(None, description="Optional state code to filter"),
    city: Optional[str] = Query(None, description="Optional city name to filter"),
    zipcode: Optional[str] = Query(None, description="Optional zipcode to filter"),
    validated_hours: int = Depends(validate_hours)
):
    """
    Fetch federal 911 emergency call data from a specified source, optionally filtered by state, city, or zipcode.
    
    Args:
        source: The name of the federal data source
        hours: Number of hours to look back (default: 24)
        state: Optional state code to filter
        city: Optional city name to filter
        zipcode: Optional zipcode to filter
    
    Returns:
        EmergencyCallResponse with count and data
    """
    try:
        # Use validated hours
        hours_to_fetch = validated_hours
        
        # Fetch data from federal API
        data = await fetch_federal_data(source, hours_to_fetch, state, city, zipcode)
        
        return EmergencyCallResponse(
            count=len(data),
            data=data
        )
    
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except httpx.HTTPStatusError as e:
        raise HTTPException(
            status_code=e.response.status_code,
            detail=str(e)
        )
    except httpx.RequestError as e:
        raise HTTPException(
            status_code=503,
            detail=str(e)
        )
    except (ValueError, RuntimeError) as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail="An unexpected error occurred"
        )

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "timestamp": datetime.utcnow().isoformat()}

@app.get("/cities")
async def list_cities():
    """List all supported cities"""
    cities_info = {}
    for city, config in CITY_REGISTRY.items():
        cities_info[city] = {
            "base_url": config["base_url"],
            "dataset_id": config["dataset_id"],
            "supports_soql": config["supports_soql"],
            "state": config.get("state", "Unknown")
        }
    return {"supported_cities": cities_info}

@app.get("/states")
async def list_states():
    """List all supported states"""
    states_info = {}
    for state, config in STATE_REGISTRY.items():
        states_info[state] = {
            "name": config["name"],
            "cities": config["cities"],
            "filters": config["filters"]
        }
    return {"supported_states": states_info}

@app.get("/federal-sources")
async def list_federal_sources():
    """List all supported federal data sources"""
    sources_info = {}
    for source, config in FEDERAL_REGISTRY.items():
        sources_info[source] = {
            "name": config["name"],
            "description": config["description"],
            "supports_soql": config["supports_soql"],
            "filters": config.get("filters", [])
        }
    return {"federal_sources": sources_info}

@app.get("/")
async def root():
    """Root endpoint with API documentation"""
    return {
        "message": "911 Emergency Call Data API",
        "version": "1.0.0",
        "endpoints": {
            "data": "/data?city=<city_name>&hours=<hours>",
            "state-data": "/state-data?state=<state_code>&hours=<hours>&city=<city>&zipcode=<zipcode>",
            "federal-data": "/federal-data?source=<source_name>&hours=<hours>&state=<state>&city=<city>&zipcode=<zipcode>",
            "health": "/health",
            "cities": "/cities",
            "states": "/states",
            "federal-sources": "/federal-sources"
        },
        "response_format": {
            "count": "Number of records returned",
            "data": "Array of emergency call records",
            "timestamp": "Response timestamp"
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)