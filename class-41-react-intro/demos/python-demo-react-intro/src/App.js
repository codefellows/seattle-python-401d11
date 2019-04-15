import './App.css'
import React, { Component } from 'react'
import StarWarsHeader from './star-wars-header/star-wars-header';
import StarWarsSearch from './star-wars-search/star-wars-search';
import StarWarsData from './star-wars-data/star-wars-data';

class App extends Component {
  constructor(props) {
    super(props)
    this.state = {
      results: [],
      promptSearch: true
    }
    this.handleSearch = this.handleSearch.bind(this)
  }

  handleSearch(searchResults) {
    this.setState({
      results: searchResults,
      promptSearch: false
    })
  }


  render() {
    return (
      <div className="App">
      
        <StarWarsHeader subTitle='May the force be with you' promptSearch={this.state.promptSearch} />

        <StarWarsSearch onSearch={this.handleSearch} />

        <StarWarsData items={this.state.results} />
        

      </div>
    )
  }
}

export default App