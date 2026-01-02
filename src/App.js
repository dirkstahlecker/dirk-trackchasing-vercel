import './App.css';
import { Analytics } from "@vercel/analytics/react"
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';
import L from 'leaflet';
import { trackDataJson } from './trackData';
import { Tabs, TabList, Tab, TabPanel } from 'react-tabs';
import 'react-tabs/style/react-tabs.css';
import { RecapsTab } from './RecapsTab';
import { FlipsTab } from './FlipsTab';

function makeMapMarkersWork() {
  delete L.Icon.Default.prototype._getIconUrl;
  L.Icon.Default.mergeOptions({
    iconRetinaUrl: require('leaflet/dist/images/marker-icon-2x.png'),
    iconUrl: require('leaflet/dist/images/marker-icon.png'),
    shadowUrl: require('leaflet/dist/images/marker-shadow.png'),
  });
}

function App() {
  makeMapMarkersWork()

  return (
    <div className="App box">
      <Analytics/>
      <h1>Dirk Trackchasing</h1>

      <p>Visit my official Trackchasers page&nbsp;
        <a href="http://www.roamingtheraceways.com/overall_individual.php?cid=303" 
          target="_blank"
          className="external-link"
        >
          here
        </a>
      </p>
      <br/>

      <Tabs>
        <TabList>
          <Tab>Race Recaps</Tab>
          <Tab>Flips</Tab>
        </TabList>

        <TabPanel><RecapsTab/></TabPanel>
        <TabPanel><FlipsTab/></TabPanel>
      </Tabs>
    </div>
  );
}

export default App;
