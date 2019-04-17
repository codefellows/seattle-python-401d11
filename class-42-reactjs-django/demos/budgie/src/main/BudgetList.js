import React from 'react'
import BudgetDetail from './BudgetDetail'

export default props => (
    <ul>
        {props.budgets.map(budget => (
            <BudgetDetail key={budget.id} budget={budget}/>
        ))}
    </ul>
)