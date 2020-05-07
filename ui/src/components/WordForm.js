import React from 'react';
import BaseActions from '../actions/BaseActions';

class WordForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {value: "", generated_text: "HALLO"};

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({value: event.target.value});
  }

  handleSubmit(event) {
    let text = BaseActions.postToGenerateText(this.state.value);
    console.log(text);
    event.preventDefault();
  }

  render() {
    return (
      <div>
      <form onSubmit={this.handleSubmit}>
        <label>
          Name:
          <input type="text" value={this.state.value} onChange={this.handleChange} />
        </label>
        <input type="submit" value="Submit"/>
      </form>
      <div>
        <p>{this.state.generated_text}</p>
      </div>
      </div>
    );
  }
}

export default WordForm;