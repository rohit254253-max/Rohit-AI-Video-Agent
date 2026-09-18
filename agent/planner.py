def create_video_plan(user_prompt: str) -> dict:
    """
    Convert a user's video idea into a structured video plan.
    """

    return {
        "prompt": user_prompt,
        "scenes": [],
        "duration": 10,
        "aspect_ratio": "16:9",
    }
