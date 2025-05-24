import streamlit as st

# Dental AI Agency - Pricing Model Estimator

def estimate_cost(call_minutes, twilio_rate=0.015, ai_rate=0.13):
    ai_cost = call_minutes * ai_rate
    twilio_cost = call_minutes * twilio_rate
    total_cost = ai_cost + twilio_cost
    return {
        "Total Minutes": call_minutes,
        "AI Cost": round(ai_cost, 2),
        "Twilio Cost": round(twilio_cost, 2),
        "Total Estimated Cost": round(total_cost, 2)
    }

st.title("Dental AI Voice Usage Cost Estimator")

st.write("Use the slider or input box to select your expected monthly call minutes.")

# Dual input: slider and number input
call_minutes_slider = st.slider("Select Monthly Call Minutes", min_value=100, max_value=1000, step=50)
call_minutes_input = st.number_input("Or enter Monthly Call Minutes", min_value=100, max_value=10000, value=call_minutes_slider, step=10)

# Use number input if it's different from slider
call_minutes = call_minutes_input if call_minutes_input != call_minutes_slider else call_minutes_slider

costs = estimate_cost(call_minutes)

st.subheader("Estimated Monthly Costs:")
st.write(f"Total Minutes: {costs['Total Minutes']} minutes ({costs['Total Minutes'] / 60:.2f} hours)")
st.write(f"AI Cost: ${costs['AI Cost']}")
st.write(f"Twilio Cost: ${costs['Twilio Cost']}")
st.write(f"Total Estimated Cost: ${costs['Total Estimated Cost']}")
