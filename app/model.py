def mock_model(input_data):
    if "fail" in str(input_data):
        raise Exception("Model failure")
    return {"prediction": len(str(input_data))}