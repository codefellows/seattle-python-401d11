import React from 'react'

export default ({ items }) => (
    <div className="results">
        <ul>
            {items.map(item => (
                <li key={item.url}>
                    <a target="_blank" href={item.url}>{item.name || item.title}</a>
                </li>
            ))}
        </ul>
    </div>
)
