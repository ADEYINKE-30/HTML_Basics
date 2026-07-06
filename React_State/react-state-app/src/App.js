import React, { Component } from 'react';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      person: {
        fullName: 'John Doe',
        bio: 'A passionate software developer with 5 years of experience building web applications.',
        imgSrc: 'https://i.pravatar.cc/200',
        profession: 'Software Engineer'
      },
      shows: false,
      mountTime: Date.now(),
      timeSinceMount: 0
    };
  }

  componentDidMount() {
    this.interval = setInterval(() => {
      this.setState({
        timeSinceMount: Math.floor((Date.now() - this.state.mountTime) / 1000)
      });
    }, 1000);
  }

  componentWillUnmount() {
    clearInterval(this.interval);
  }

  toggleShow = () => {
    this.setState(prevState => ({
      shows: !prevState.shows
    }));
  };

  formatTime(seconds) {
    const hours = Math.floor(seconds / 3600);
    const minutes = Math.floor((seconds % 3600) / 60);
    const secs = seconds % 60;
    return `${hours}h ${minutes}m ${secs}s`;
  }

  render() {
    const { person, shows, timeSinceMount } = this.state;

    return (
      <div style={styles.container}>
        <h1 style={styles.heading}>React State App</h1>
        
        <div style={styles.timer}>
          <strong>Time since component mounted:</strong> {this.formatTime(timeSinceMount)}
        </div>

        <button style={styles.button} onClick={this.toggleShow}>
          {shows ? 'Hide Profile' : 'Show Profile'}
        </button>

        {shows && (
          <div style={styles.profile}>
            <img src={person.imgSrc} alt={person.fullName} style={styles.image} />
            <h2>{person.fullName}</h2>
            <p><strong>Profession:</strong> {person.profession}</p>
            <p><strong>Bio:</strong> {person.bio}</p>
          </div>
        )}
      </div>
    );
  }
}

const styles = {
  container: {
    maxWidth: '600px',
    margin: '0 auto',
    padding: '40px 20px',
    textAlign: 'center',
    fontFamily: 'Arial, sans-serif'
  },
  heading: {
    color: '#333',
    marginBottom: '20px'
  },
  timer: {
    fontSize: '18px',
    marginBottom: '20px',
    padding: '10px',
    backgroundColor: '#f0f0f0',
    borderRadius: '5px'
  },
  button: {
    padding: '12px 30px',
    fontSize: '16px',
    backgroundColor: '#007bff',
    color: 'white',
    border: 'none',
    borderRadius: '5px',
    cursor: 'pointer',
    marginBottom: '20px'
  },
  profile: {
    marginTop: '20px',
    padding: '20px',
    backgroundColor: '#f9f9f9',
    borderRadius: '10px',
    boxShadow: '0 2px 5px rgba(0,0,0,0.1)'
  },
  image: {
    width: '150px',
    height: '150px',
    borderRadius: '50%',
    objectFit: 'cover',
    marginBottom: '15px'
  }
};

export default App;