import React from 'react';

const FilterBar = ({ onFilterChange }) => {
    const handleChange = (event) => {
        const { name, value } = event.target;
        onFilterChange(name, value);
    };

    return (
        <div className="filter-bar">
            <select name="uploadDate" onChange={handleChange}>
                <option value="">Upload Date</option>
                <option value="today">Today</option>
                <option value="week">This Week</option>
                <option value="month">This Month</option>
            </select>

            <select name="videoDuration" onChange={handleChange}>
                <option value="">Duration</option>
                <option value="short">Short (&lt; 4 min)</option>
                <option value="long">Long (&gt; 20 min)</option>
            </select>

            <select name="category" onChange={handleChange}>
                <option value="">Category</option>
                <option value="music">Music</option>
                <option value="sports">Sports</option>
                <option value="news">News</option>
            </select>
        </div>
    );
};

export default FilterBar;
