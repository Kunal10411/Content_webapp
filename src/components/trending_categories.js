import React from 'react';

const categories = ['Music', 'Sports', 'News', 'Gaming', 'Education'];

const TrendingCategories = ({ onCategorySelect }) => {
    return (
        <div className="categories">
            {categories.map((category) => (
                <button 
                    key={category} 
                    onClick={() => onCategorySelect(category)}
                    className="category-btn"
                >
                    {category}
                </button>
            ))}
        </div>
    );
};

export default TrendingCategories;
