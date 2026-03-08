CAUSE_RULES = {
 "frustration": ["angry","frustrated","upset","concerning"],
 "delivery_failure": ["never received","not delivered","marked delivered"],
 "replacement_requested": ["send a replacement","replacement shipped"],
 "investigation": ["start an investigation","file a claim"]
}


def detect_factors(turns):
    factors = []

    for name, keys in CAUSE_RULES.items():
        if any(k in t["text"].lower() for t in turns for k in keys):
            factors.append(name)

    return factors

