def fill_model_attributes(
    model_to: any,
    model_from: any,
    exclude_unset=True,
):
    for name, value in model_from.model_dump(exclude_unset=exclude_unset).items():
        setattr(model_to, name, value)
    return model_to
