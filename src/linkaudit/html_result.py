"""
License GPL3

(C) 2024-2025 Created by Maikel Mardjan - https://nocomplexity.com/

Function to create a HTML result file of a linkaudit run

"""

import os


def generate_html_table(data):
    """
    Generates an HTML table for entries with status != 200.

    Args:
        data (list of dict): A list of dictionaries with 'line_number', 'url', and 'status' keys.

    Returns:
        str: A string containing the HTML table.
    """
    # Start the HTML table
    html_table = """
    <table class="table table-striped table-bordered table-hover">    
        <thead>
            <tr >
                <th>Line Number</th>
                <th>URL</th>
                <th>Status Code</th>
            </tr>
        </thead>
        <tbody>
    """

    # Add rows for entries with status != 200
    for entry in data:
        if entry["status"] != 200:
            html_table += f"""
            <tr>
                <td>{entry['line_number']}</td>
                <td>{entry['url']}</td>
                <td>{entry['status']}</td>
            </tr>
            """

    # Close the table
    html_table += """
        </tbody>
    </table>
    """
    return html_table


def create_output_htmlfile(result, filename):
    """Creates a clean output.html file of the input given"""
    FILENAME = filename
    output = '<!DOCTYPE html><html lang="en-US"><head>    <meta charset="UTF-8"/><title> Standard Generated Output file </title></head>'  # html charset UTF-8!
    output += """
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Styled Table</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css">  </head> <body>
    """      # Give the output a bootstrap look    
    output += '<body class="mt-3 mx-4">'
    output += result
    output += '</body>'
    with open(FILENAME, "w") as f:
        f.write(output)
    current_directory = os.getcwd()  # gets the current directory
    result_location = current_directory + "/" + FILENAME
    print(f"Result file written! Check file : file://{result_location}")
