# f1-web-streamlit
A web application built with **Streamlit** and **FastF1** that allows users to compare the performance of two Formula 1 drivers during any race weekend session.

The application retrieves official timing data, calculates key statistics, and generates an interactive lap time comparison chart.

---

## Running the Application

Start the Streamlit server:

```bash
streamlit run f1web.py
```

The application will automatically open in your default web browser.

---

## How to Use

1. Select the season year.
2. Enter the Grand Prix name (in English, e.g. `Spain`, `Monaco`, `Silverstone`).
3. Select the session type.
4. Enter the three-letter driver codes (e.g. `VER`, `HAM`, `NOR`, `PIA`).
5. Click **Analyze**.

The application will display:

- Average lap time for each driver
- Fastest lap for each driver
- Lap-by-lap comparison chart
- Option to download the graph as a PNG image

---

## Built With

- Python
- Streamlit
- FastF1
- Matplotlib
- Pandas

---

## Project Structure

```
FastF1-Race-Analyzer/
│
├── f1web.py
├── requirements.txt
└── README.md
```

---

## Future Improvements

- Team colors automatically applied to charts
- Telemetry comparison
- Sector time analysis
- Tire strategy visualization
- Circuit map
- Race pace analysis
- Automatic driver selection from a dropdown menu
- Sprint session support

---

## Contributing

Contributions, suggestions, and bug reports are welcome! Feel free to open an issue or submit a pull request.

---

## License

This project is licensed under the MIT License (for more details read the LICENSE file).

---

## Acknowledgements

- **FastF1** for providing an excellent API to access official Formula 1 timing data.
- **Streamlit** for making Python web applications simple and interactive.
- Formula 1 for the publicly available timing data used by FastF1.
