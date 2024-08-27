def load_css():
    return """
        <style>
        /* General Styles */
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f4f4f9;
            color: #333;
        }
        
        /* Button Styles */
        .stButton button {
            background-color: #007BFF;
            color: white;
            font-size: 16px;
            padding: 12px 24px;
            border-radius: 5px;
            transition: background-color 0.3s ease, transform 0.2s ease;
            border: none;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        
        .stButton button:hover {
            background-color: #0056b3;
            transform: translateY(-1px);
        }
        
        /* Title Styles */
        .stTitle h1 {
            color: #343a40;
            font-weight: 700;
            text-align: center;
            margin-bottom: 20px;
        }
        
        .stTitle h2 {
            color: #6c757d;
            text-align: center;
            font-size: 1.5rem;
        }
        
        /* Markdown Styles */
        .stMarkdown {
            margin: 20px 0;
        }
        
        /* Result Box Styles */
        .result {
            padding: 15px;
            border-radius: 5px;
            background-color: #fff;
            border: 1px solid #ddd;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
        }
        
        /* Alert Styles */
        .stAlert {
            border-radius: 5px;
            padding: 15px;
            margin-bottom: 20px;
        }
        </style>
    """
