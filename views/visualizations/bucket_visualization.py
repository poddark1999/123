import plotly.graph_objects as go
from plotly.offline import plot

def bucket_completion(bucket):
	labels = ['Allocated amount', 'Remaining Amount']
	values = [bucket.current_amount, bucket.goal - bucket.current_amount]

	fig = go.Figure(data=[go.Pie(labels=labels, values=values, hoverinfo='label+percent')])
	fig.update_layout(
		title={
			'text': "State of completion",
			'x': 0.5,  # Center the title
			'y': 0.9,  # Adjust the vertical position of the title
			'xanchor': 'center',  # Center the title horizontally
			'yanchor': 'top',  # Position the title at the top
			'font': {'size': 16}  # Set the font size and weight
		},
		width=500,
		height=400,
  		paper_bgcolor='rgba(240, 240, 240, 1)'# Set the background color to light blue
	)
	fig.update_traces(textinfo='percent', textposition='inside')
	fig.update_layout(legend=dict(orientation="h"))

	return plot(fig, output_type='div')

