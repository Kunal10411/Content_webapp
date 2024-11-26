import React, { useState } from 'react';

const Playlist = ({ videos }) => {
    const [playlist, setPlaylist] = useState([]);

    const addToPlaylist = (video) => {
        setPlaylist([...playlist, video]);
    };

    return (
        <div className="playlist-container">
            <h2>Your Playlist</h2>
            <ul>
                {playlist.map((video, index) => (
                    <li key={index}>
                        <img src={video.thumbnail_url} alt={video.title} />
                        <p>{video.title}</p>
                    </li>
                ))}
            </ul>
            <div className="videos">
                {videos.map((video) => (
                    <div key={video.video_id} className="video">
                        <img src={video.thumbnail_url} alt={video.title} />
                        <p>{video.title}</p>
                        <button onClick={() => addToPlaylist(video)}>Add to Playlist</button>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default Playlist;
