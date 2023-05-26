import * as React from 'react';
import PropTypes from 'prop-types';
import Tabs from '@mui/material/Tabs';
import Tab from '@mui/material/Tab';
import Typography from '@mui/material/Typography';
import Box from '@mui/material/Box';
import MainPage from '../../pages/MainPage';
import MyPage from '../../pages/MyPage';

import AppHeader from '../../common/AppHeader'

function TabPanel(props) {
  const { children, value, index, ...other } = props;

  return (
    <div
      role="tabpanel"
      hidden={value !== index}
      id={`simple-tabpanel-${index}`}
      aria-labelledby={`simple-tab-${index}`}
      {...other}
    >
      {value === index && (
        <Box sx={{ p: 3 }}>
          <Typography>{children}</Typography>
        </Box>
      )}
    </div>
  );
}

TabPanel.propTypes = {
  children: PropTypes.node,
  index: PropTypes.number.isRequired,
  value: PropTypes.number.isRequired,
};

function a11yProps(index) {
  return {
    id: `simple-tab-${index}`,
    'aria-controls': `simple-tabpanel-${index}`,
  };
}

export default function HeaderTab() {
  const [value, setValue] = React.useState(0);

  const handleChange = (event, newValue) => {
    setValue(newValue);
  };

  return (
    <Box sx={{ width: '100%' }}>
      <AppHeader/>
      <Box sx={{ borderBottom: 1, borderColor: 'divider', backgroundColor: '#F5F1F1' }}>
        <Tabs value={value} onChange={handleChange} aria-label="basic tabs example"
                TabIndicatorProps={{ style: { background: "#000" } }}
                textColor="inherit">
          <Tab label="메이트" {...a11yProps(0)} />
          <Tab label="깃만추" {...a11yProps(1)} />
        </Tabs>
      </Box>
      <TabPanel value={value} index={0}>
        <MainPage/>
        {/* Main */}
      </TabPanel>
      <TabPanel value={value} index={1}>
        <MyPage/>
        {/* My */}
      </TabPanel>
    </Box>
  );
}