import React, { useState } from 'react';
import './App.css';

function App() {
  const [inputValue, setInputValue] = useState('');
  const [messages, setMessages] = useState([]);

  const handleInputChange = (event) => {
    setInputValue(event.target.value);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    if (inputValue.trim() !== '') {
      setMessages([...messages, inputValue]);
      setInputValue('');
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Chat Add-On</h1>
        <div className="message-area">
          {messages.map((message, index) => (
            <div key={index} className="message">{message}</div>
          ))}
        </div>
        <form onSubmit={handleSubmit}>
          <input
            type="text"
            value={inputValue}
            onChange={handleInputChange}
            placeholder="Type your message here..."
          />
          <button type="submit">Send</button>
        </form>
      </header>
    </div>
  );
}

export default App;
