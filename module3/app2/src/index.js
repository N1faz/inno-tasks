import React from 'react';
import ReactDOM from 'react-dom';

// стили 
const styles = {
    container: {
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        height: '100vh',
        fontSize: '2rem',
        fontFamily: 'Arial, sans-serif',
        backgroundColor: '#f0f8ff'
    }
};

// компонент приложения
function App() {
    return (
        <div style={styles.container}>
              Мой статичный сайт!
        </div>
    );
}

// рендеринг в root
ReactDOM.render(<App />, document.getElementById('root'));
