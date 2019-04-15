import React from 'react';

function getSearchClass(promptSearch) {
    if (promptSearch) {
        return 'search-pending';
    } else {
        return 'search-complete';
    }
}

export default ({subTitle, promptSearch}) => (
    <header>
        <h1>Star Wars Stuff</h1>
        <h2>{subTitle}</h2>
        <h3 className={getSearchClass(promptSearch)}>
            {promptSearch ? 'Begin your search...' : 'Have you found what you seek?'}
        </h3>
    </header>
)