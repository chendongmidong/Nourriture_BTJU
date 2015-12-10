package com.nourriture.app;

import android.content.Intent;
import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.TextView;

/**
 * Created by Simon on 23-Nov-15.
 */
public class TabFragment1 extends Fragment {
    public final static String PERSONAL_SETTING = "com.nourriture.app.p_setting"; //PersonalSettingActivity
    public final static String SETTING = "";
    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.tab_fragment_1, container, false);
        TextView personal_setting = (TextView) view.findViewById(R.id.personal_setting);

        personal_setting.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent();
                intent.setAction(PERSONAL_SETTING);
                startActivity(intent);
            }
        });
        return view;
    }
}
