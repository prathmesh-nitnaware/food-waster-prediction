<h1>🌟 Local Food Wastage Management System</h1>
<h2>🌍 A Data-Driven Approach to Social Good</h2>
<hr/>

<h2>🔎 Overview</h2>
<p>
  This project tackles the <b>global problem of food wastage</b> by building a structured platform that connects 
  <b>surplus food providers</b> with <b>people in need</b>.  
  It leverages a <b>user-friendly web application</b> and <b>machine learning models</b> to optimize food distribution 
  and make a <b>real-world impact</b>.
</p>

<hr/>

<h2>💡 Project Highlights</h2>
<ul>
  <li>🖥️ <b>Intuitive Web App</b> – Built with <b>Streamlit</b> for a clean, interactive UI.</li>
  <li>🤖 <b>Intelligent Predictions</b> – Two ML models offer insights to predict demand & reduce wastage.</li>
  <li>🗄️ <b>Robust Backend</b> – Integrated with <b>SQL</b> for secure, structured data storage.</li>
  <li>🌱 <b>Community-Focused</b> – Designed for <b>social good</b>, reducing waste & fighting food insecurity.</li>
</ul>

<hr/>

<h2>🚀 Tech Stack</h2>
<ul>
  <li>🐍 <b>Python</b> – Core logic & data processing</li>
  <li>🎨 <b>Streamlit</b> – Dynamic, responsive web interface</li>
  <li>📊 <b>Pandas & Scikit-learn</b> – Data analysis & ML modeling</li>
  <li>📦 <b>Joblib</b> – Model serialization & deployment</li>
  <li>🗄️ <b>SQL</b> – Structured, reliable database</li>
</ul>

<hr/>

<h2>🤖 Machine Learning Models</h2>

<h3>🔹 Model 1: Claim Probability Predictor</h3>
<ul>
  <li><b>Type:</b> Random Forest Classifier</li>
  <li><b>Objective:</b> Predict whether a food listing will be claimed</li>
</ul>

<table>
  <tr>
    <th>Metric</th>
    <th>Precision</th>
    <th>Recall</th>
    <th>F1-Score</th>
  </tr>
  <tr>
    <td>Class 0 (Not Claimed)</td>
    <td>0.00</td>
    <td>0.00</td>
    <td>0.00</td>
  </tr>
  <tr>
    <td>Class 1 (Claimed)</td>
    <td>0.50</td>
    <td>1.00</td>
    <td>0.67</td>
  </tr>
</table>

<h3>🔹 Model 2: Quantity Claimed Predictor</h3>
<ul>
  <li><b>Type:</b> Gradient Boosting Regressor</li>
  <li><b>Objective:</b> Predict the <b>exact quantity</b> of food claimed</li>
</ul>

<table>
  <tr>
    <th>Metric</th>
    <th>Score</th>
  </tr>
  <tr>
    <td>Mean Squared Error (MSE)</td>
    <td>1.15</td>
  </tr>
  <tr>
    <td>R-squared (R²)</td>
    <td>0.50</td>
  </tr>
</table>

<hr/>



