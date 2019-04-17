import React from 'react'
import BudgetList from './BudgetList'
import BudgetForm from './BudgetForm'
import superagent from 'superagent'

export default class Main extends React.Component {

    constructor(props) {
        super(props)
        this.state = {
            budgets: []
        }
    }


    componentDidMount() {
        // initial async stuff. like a data fetch api call
        const url = 'http://localhost:8000/api/v1/budgets/'

        superagent
            .get(url)
            .set('Authorization', `Token ${this.props.token}`)
            .then(response => {
                this.setState({
                    budgets : response.body
                })
            })
    }


    render() {
        return (<section>
            <h1>Main</h1>
            <BudgetList budgets={this.state.budgets} />
            <BudgetForm token={this.props.token} />
        </section>)
    }
}