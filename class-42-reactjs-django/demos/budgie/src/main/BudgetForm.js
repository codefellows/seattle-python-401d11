import React, { Component } from 'react'
import superagent from 'superagent'

export default class BudgetForm extends Component {

    constructor(props) {
        super(props)
        this.state = {
            name: '',
            budget: ''
        }
        this.onChange = this.onChange.bind(this)
        this.onSubmit = this.onSubmit.bind(this)
    }

    onChange(event) {
        this.setState({
            [event.target.name] : event.target.value
        })
    }

    onSubmit(event) {
        event.preventDefault()
        this.fetchBudgets()
    }

    async fetchBudgets() {
        const url = 'http://localhost:8000/api/v1/budgets/'

        const response = await superagent
            .post(url)
            .send({
                name : this.state.name,
                total_budget : this.state.budget,
            })
            .set('Authorization',`Token ${this.props.token}`)

        console.log(response.body)
    }

    render() {
        return (
            <form onSubmit={this.onSubmit}>
                <label>Name
                <input 
                    type="text" 
                    name="name" 
                    value={this.state.name}
                    onChange={this.onChange}
                />
                </label>
                <label>Budget
                <input 
                    type="number" 
                    name="budget" 
                    value={this.state.budget}
                    onChange={this.onChange}
                />
                </label>
                <button>submit</button>
            </form>
        )
    }
}