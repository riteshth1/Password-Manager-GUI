<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>

<h1>Password Manager</h1>
<p>This is a simple Password Manager application built using Python and Tkinter. The application allows users to generate strong passwords and save them along with their website and email information. It also features the ability to copy the generated password to the clipboard for easy use.</p>

<h2>Features</h2>
<ul>
    <li><strong>Password Generation</strong>: Generates a random, strong password containing letters, numbers, and symbols.</li>
    <li><strong>Save Password</strong>: Saves the website, email/username, and generated password to a file.</li>
    <li><strong>Clipboard Copy</strong>: Automatically copies the generated password to the clipboard.</li>
</ul>

<h2>Requirements</h2>
<ul>
    <li>Python 3.x</li>
    <li>Tkinter (usually comes pre-installed with Python)</li>
    <li>pyperclip</li>
</ul>

<h2>Installation</h2>
<ol>
    <li><strong>Clone the repository</strong>:
        <pre><code>git clone https://github.com/your-username/password-manager.git</code></pre>
    </li>
    <li><strong>Navigate to the project directory</strong>:
        <pre><code>cd password-manager</code></pre>
    </li>
    <li><strong>Install dependencies</strong>:
        <pre><code>pip install pyperclip</code></pre>
    </li>
</ol>

<h2>Usage</h2>
<ol>
    <li><strong>Run the application</strong>:
        <pre><code>python password_manager.py</code></pre>
    </li>
    <li><strong>Generate a Password</strong>:
        <ul>
            <li>Click the "Generate Password" button to generate a strong password.</li>
        </ul>
    </li>
    <li><strong>Save Password</strong>:
        <ul>
            <li>Enter the website and email/username.</li>
            <li>Click the "Add" button to save the details.</li>
        </ul>
    </li>
    <li><strong>Copy Password</strong>:
        <ul>
            <li>The generated password is automatically copied to the clipboard for easy pasting.</li>
        </ul>
    </li>
</ol>

<h2>Project Structure</h2>
<ul>
    <li><code>password_manager.py</code>: Main application file containing the Tkinter GUI and logic for generating and saving passwords.</li>
    <li><code>logo.png</code>: Logo image displayed in the application.</li>
    <li><code>passwordManager</code>: Text file where the saved passwords are stored.</li>
</ul>

<h2>Contributing</h2>
<p>Contributions are welcome! If you have any suggestions or improvements, feel free to submit a pull request.</p>

<h2>License</h2>
<p>This project is licensed under the MIT License. See the <a href="LICENSE">LICENSE</a> file for details.</p>

<h2>Acknowledgements</h2>
<ul>
    <li><a href="https://docs.python.org/3/library/tkinter.html">Tkinter</a> - Python's standard GUI library.</li>
    <li><a href="https://pypi.org/project/pyperclip/">pyperclip</a> - Cross-platform clipboard module for Python.</li>
</ul>

</body>
</html>
