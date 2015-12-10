package com.nourriture.app.setting;

import android.os.Bundle;
import android.support.v4.app.FragmentActivity;
import android.view.Window;
import com.nourriture.app.R;

/**
 * Created by liuyifan on 15/12/9.
 */
public class PersonalSettingActivity extends FragmentActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState){
        super.onCreate(savedInstanceState);
        requestWindowFeature(Window.FEATURE_NO_TITLE);
        setContentView(R.layout.setting_main);
    }
}
