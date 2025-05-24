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

call_minutes = st.slider("Select Monthly Call Minutes", min_value=100, max_value=1000, step=50)

costs = estimate_cost(call_minutes)

st.subheader("Estimated Monthly Costs:")
st.write(f"Total Minutes: {costs['Total Minutes']} minutes")
st.write(f"AI Cost: ${costs['AI Cost']}")
st.write(f"Twilio Cost: ${costs['Twilio Cost']}")
st.write(f"Total Estimated Cost: ${costs['Total Estimated Cost']}")
