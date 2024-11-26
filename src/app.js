import React, { useState, useEffect } from 'react';
import SearchBar from './components/SearchBar';
import FilterBar from './components/filterbar';
import TrendingCategories from './components/TrendingCategories';
import Playlist from './components/playlist';
import VideoCard from './components/VideoCard';
import './styles/App.css';

const App = () => {
    const [videos, setVideos] = useState([]);
    const [filters, setFilters] = useState({});
    const [category, setCategory] = useState('');

    useEffect(() => {
        // Fetch trending videos or apply filters
        fetchVideos();
    }, [filters, category]);

    const fetchVideos = async () => {
        let query = `?category=${category}`;
        Object.keys(filters).forEach((key) => {
            if (filters[key]) query += `&${key}=${filters[key]}`;
        });

        const response = await fetch(`/api/videos${query}`);
        const data = await response.json();
        setVideos(data.videos);
    };

    return (
        <div className="container">
            <h1>Trendly - Trending Videos</h1>
            <SearchBar />
            <FilterBar onFilterChange={(name, value) => setFilters({ ...filters, [name]: value })} />
            <TrendingCategories onCategorySelect={(cat) => setCategory(cat)} />
            <Playlist videos={videos} />
            <div className="video-list">
                {videos.map((video) => (
                    <VideoCard key={video.video_id} video={video} />
                ))}
            </div>
        </div>
    );
};

export default App;
