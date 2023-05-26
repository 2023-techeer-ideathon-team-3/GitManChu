import {
    Box
} from '@mui/material';
import InfoBox from '../components/MyPage/InfoBox';
import MainProfileBox from '../components/MyPage/MainProfileBox';
import React from 'react';


export default function MyPage() {

    return(
        <Box>
            {/* <Main/> */}

            <MainProfileBox/>

            <InfoBox/>
        </Box>
    )
}