import Head from 'next/head'
import { Container, Row, Card, Button } from 'react-bootstrap'

export default function Home() {
  return (
    <Container className="md-container">
      <Head>
        <title>Dirk Trackchasing</title>
      </Head>

      <a href={"/recaps/5-19-23_Clinton_County_Speedway.pdf"} target="_blank">5-19-23 Clinton County Speedway</a>
      
      <footer className="cntr-footer">

      </footer>
    </Container>
  )
}
