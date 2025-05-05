// src/components/NewsCard.jsx
import React, { useState } from 'react';

const NewsCard = ({ article }) => {
  const [summary, setSummary] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSummarize = async () => {
    setLoading(true);
    try {
      const response = await fetch("http://localhost:8000/scraper/summarize/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ url: article.link }),
      });

      const data = await response.json();
      setSummary(data.summary || "No summary available.");
    } catch (error) {
      console.error("Error fetching summary", error);
      setSummary("Failed to fetch summary.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="news-item">
      <h3>{article.title}</h3>
      <a href={article.link} target="_blank" rel="noopener noreferrer">
        Read More
      </a>

      {/* Summarize button */}
      <button onClick={handleSummarize} disabled={loading}>
        {loading ? "Loading..." : "Summarize"}
      </button>

      {/* Display summary */}
      {summary && (
        <div className="summary-container">
          <h4>Summary:</h4>
          <p>{summary}</p>
        </div>
      )}
    </div>
  );
};

export default NewsCard;
