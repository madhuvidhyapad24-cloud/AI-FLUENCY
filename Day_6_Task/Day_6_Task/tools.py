
"""Tool definitions for the FarmAssist agriculture assistant."""

TOOLS = {
    "estimate_water_budget": {
        "description": "Estimate daily irrigation water for a farm.",
        "parameters": {
            "type": "object",
            "properties": {
                "area_acres": {"type": "number", "minimum": 0.1, "maximum": 10000},
                "water_mm_per_day": {"type": "number", "minimum": 0, "maximum": 100},
                "crop": {"type": "string", "minLength": 1}
            },
            "required": ["area_acres", "water_mm_per_day", "crop"],
            "additionalProperties": False
        }
    },
    "irrigation_tips": {
        "description": "Give water-saving irrigation tips.",
        "parameters": {
            "type": "object",
            "properties": {
                "crop": {"type": "string", "minLength": 1},
                "method": {
                    "type": "string",
                    "enum": ["drip", "sprinkler", "flood", "unknown"]
                }
            },
            "required": ["crop", "method"],
            "additionalProperties": False
        }
    }
}


def estimate_water_budget(area_acres, water_mm_per_day, crop):
    litres = area_acres * 4046.8564224 * water_mm_per_day
    return {
        "crop": crop,
        "area_acres": area_acres,
        "estimated_litres_per_day": round(litres, 2),
        "note": "Approximate estimate; actual needs depend on field conditions."
    }


def irrigation_tips(crop, method):
    tips = {
        "drip": ["Check emitters", "Repair leaks", "Water near roots"],
        "sprinkler": ["Avoid windy hours", "Check nozzle coverage"],
        "flood": ["Reduce runoff", "Check field levelling"],
        "unknown": ["Check soil moisture", "Repair leaks"]
    }
    return {"crop": crop, "method": method, "tips": tips[method]}
