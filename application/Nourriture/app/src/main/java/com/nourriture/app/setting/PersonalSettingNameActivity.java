package com.nourriture.app.setting;

import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.support.v4.app.FragmentActivity;
import android.view.Window;
import com.nourriture.app.R;

/**
 * Created by liuyifan on 15/12/11.
 */
public class PersonalSettingNameActivity extends FragmentActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState){
        super.onCreate(savedInstanceState);
        requestWindowFeature(Window.FEATURE_NO_TITLE);
        setContentView(R.layout.setting_name);

//        String name = getIntent().getStringExtra("name");
//        boolean isTwoPane = getIntent().getBooleanExtra("isTwoPane", false);
//
//        PersonalSettingNameFragment personalSettingNameFragment =
//                (PersonalSettingNameFragment) getSupportFragmentManager().findFragmentById(R.id.setting_name_frag);
//        personalSettingNameFragment.setName(name);
    }

    public static void actionStart(Context context, String name, boolean isTwoPane){
        Intent intent = new Intent(context, PersonalSettingNameActivity.class);
        intent.putExtra("name", name);
        intent.putExtra("isTwoPane", isTwoPane);
        context.startActivity(intent);
    }
}
