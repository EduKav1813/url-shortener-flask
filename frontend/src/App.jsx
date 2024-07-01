import React, { useState } from "react";
import "./App.css";
import config from "./config";

function App() {
  const [longUrl, setLongUrl] = useState("");
  const [shortUrl, setShortUrl] = useState("");
  const [code, setCode] = useState("");
  const [error, setError] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");
    setShortUrl("");
    setCode("");

    try {
      const response = await fetch(config.apiUrl + "register/", {
        method: "POST",
        headers: {
          "Content-type": "application/json",
          Accept: "application/json",
        },
        body: JSON.stringify({ url: longUrl }),
      });

      if (!response.ok) {
        throw new Error("Failed to shorten URL");
      }

      const data = await response.json();
      setShortUrl(data.shortUrl);
      setCode(config.apiUrl + "redirect/" + data.code);
    } catch (error) {
      setError(error.message);
    }
  };

  return (
    <div className="App">
      <h1>URL Shortener</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="longUrl">Enter URL to shorten:</label>
          <input
            type="url"
            id="longUrl"
            value={longUrl}
            onChange={(e) => setLongUrl(e.target.value)}
            required
          />
        </div>
        <button type="submit">Shorten URL</button>
      </form>
      {shortUrl && (
        <div>
          <h2>Shortened URL:</h2>
          <a href={shortUrl} target="_blank" rel="noopener noreferrer">
            {shortUrl}
          </a>
        </div>
      )}
      {error && <p className="error">{error}</p>}
      {code && <p className="code">{code}</p>}
    </div>
  );
}

export default App;
