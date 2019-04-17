import React from 'react'
import LoginForm from './LoginForm'

export default props => (
    <section>
        <h1>Landing</h1>
        <LoginForm onLogin={props.onLogin} />
    </section>
)