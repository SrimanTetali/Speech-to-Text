def load_css():
    return """
        <style>
        .stButton button {
            background-color: #007BFF;
            color: white;
            font-size: 18px;
            padding: 10px 24px;
            border-radius: 8px;
            transition: background-color 0.3s ease;
            border: none;
        }
        .stButton button:hover {
            background-color: #0056b3;
        }
        .stTitle h1 {
            color: #343a40;
            font-weight: 700;
            text-align: center;
            margin-bottom: 10px;
        }
        .stTitle h2 {
            color: #6c757d;
            text-align: center;
        }
        .stMarkdown {
            margin: 20px 0;
        }
        .result {
            padding: 10px;
            border-radius: 5px;
            background-color: #f8f9fa;
            border-left: 5px solid #007BFF;
            margin-bottom: 20px;
        }
        .stAlert {
            border-radius: 8px;
            padding: 20px;
            margin-bottom: 20px;
        }
        </style>
    """
