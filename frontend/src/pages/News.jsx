// src/Pages/news.jsx 
import { useState, useEffect } from "react";
import NewsCard from "../components/NewsCard";
import "../styles/News.css";

function News() {
    const [news, setNews] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        fetch("http://localhost:8000/scraper/scrape/")  // Ensure the URL is correct
            .then(res => res.json())
            .then(data => {
                if (Array.isArray(data)) {
                    setNews(data);  // Set the news if it's an array
                } else {
                    console.error("Received data is not an array:", data);
                }
                setLoading(false);
            })
            .catch(err => {
                console.error("Error fetching news", err);
                setLoading(false);
            });
    }, []);

    return (
        <div className="news-container">
            <h1>Latest News</h1>
            {loading ? (
                <p>Loading news...</p>
            ) : (
                news.length > 0 ? (
                    news.map((article, i) => <NewsCard key={i} article={article} />)
                ) : (
                    <p>No news available</p>
                )
            )}
        </div>
    );
}

export default News;
