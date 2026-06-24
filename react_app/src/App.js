import Card from 'react-bootstrap/Card';
import Col from 'react-bootstrap/Col';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Name from './Name';
import Price from './Price';
import Description from './Description';
import Image from './Image';
import './App.css';

const firstName = 'Alex';

function App() {
  const greetingName = firstName.trim() || 'there!';

  return (
    <div className="app-shell">
      <Container>
        <Row className="justify-content-center">
          <Col xs={12} lg={9} xl={8}>
            <Card className="product-card">
              {firstName ? <Image /> : null}
              <Card.Body>
                <div className="product-label">Featured Product</div>
                <Name />
                <Price />
                <Description />
              </Card.Body>
            </Card>
            <div className="greeting">Hello, <strong>{greetingName}</strong></div>
          </Col>
        </Row>
      </Container>
    </div>
  );
}

export default App;