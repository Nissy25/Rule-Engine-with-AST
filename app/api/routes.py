from fastapi import APIRouter, HTTPException
from app.services.rule_engine import create_rule, combine_rules, evaluate_rule

router = APIRouter()

@router.post("/create_rule")
def create_rule_endpoint(rule_string: str):
    try:
        rule = create_rule(rule_string)
        return {"AST": rule}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/combine_rules")
def combine_rules_endpoint(rules: list):
    try:
        # Create an AST for each rule
        asts = [create_rule(rule) for rule in rules]
        
        # Combine the ASTs into one
        combined_rule = combine_rules(asts)
        
        return {"combined_AST": combined_rule}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/evaluate_rule")
def evaluate_rule_endpoint(data: dict, rule_string: str):
    try:
        rule = create_rule(rule_string)
        result = evaluate_rule(rule, data)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



