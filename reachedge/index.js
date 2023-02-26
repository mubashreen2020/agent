import React from 'react';
import ReactDOM from 'react-dom';

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = { message: "" };
  }

  componentDidMount() {
    fetch('/api/hello')
      .then(response => response.json())
      .then(data => this.setState({ message: data.message }));
  }

  render() {
    return (
      <div>
        <h1>Hello from React</h1>
        <p>{this.state.message}</p>
      </div>
    );
  }
}

ReactDOM.render(<App />, document.getElementById('root'));
